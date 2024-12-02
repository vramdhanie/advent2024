from pydantic import BaseModel


class Base(BaseModel):
    test: bool = True
    puzzle: int = 1
