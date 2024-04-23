from pydantic import BaseModel


class NERData(BaseModel):
    text_input: str
    domain: str | None = None
    description: str | None = None
    labels: str | None = None
