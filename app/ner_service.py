import ast
import re

from loguru import logger
from promptify import Prompter, Pipeline, OpenAI

from app.models import NERData
from app.settings import settings
from app.sample_data import one_shot

model = OpenAI(api_key=settings.openai_key)
prompter = Prompter('ner.jinja')
pipe = Pipeline(prompter, model, structured_output=False)


class NERService:
    DOMAIN = "real estate"
    LABELS = [
        "INTENT", "TWO STORY", "BUDGET", "PETS", "GARAGE",
        "POOL", "AC", "FLOOR SPACE", "WATERFRONT", "VIEW", "YEAR BUILT"
    ]
    DESCRIPTION = ("Below Paragraph is a description a home someone is interested in buying. "
                   "t includes a number of different features they desire, which are all related "
                   "to home features and amenities.")

    @classmethod
    def process(cls, data: NERData) -> list[dict]:
        try:
            result = pipe.fit(
                domain=cls.DOMAIN,
                text_input=data.text_input,
                description=cls.DESCRIPTION,
                labels=cls.LABELS,
                one_shot=one_shot
            )

            return cls.serialize_response(result)
        except Exception as e:
            logger.error(f"Error occurred: {str(e)}")
            raise

    @classmethod
    def serialize_response(cls, resp: list[dict]) -> list[dict]:
        result: list[dict] = []

        for elem in resp:
            for choice in elem.get("choices", []):
                message = choice.get("message", {}).get("content")
                if not message:
                    continue
                result.extend(cls._convert_to_dict(message))

        return result

    @classmethod
    def _convert_to_dict(cls, data: str) -> list[dict]:
        try:
            return cls.parse_str_data(data)
        except Exception as e:
            logger.error(f"Error occurred while loading: {e}")
            raise

    @staticmethod
    def parse_str_data(data: str) -> list[dict]:
        # Match all occurrences of dictionaries using regular expressions
        dict_pattern = r"{[^{}]*}"
        dicts = re.findall(dict_pattern, data)

        # Parse each matched dictionary string into a Python dictionary
        parsed_data = [ast.literal_eval(d) for d in dicts]

        return parsed_data
