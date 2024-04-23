from pydantic import BaseModel


class NERData(BaseModel):
    text_input: str
