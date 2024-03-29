import datetime

from pydantic import BaseModel, field_validator


class AnswerCreate(BaseModel):
    content: str
    
    @field_validator("content")
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("NOT_ALLOW_EMPTY_VALUE")
        return v

        
class Answer(BaseModel):
    id: int
    content: str
    create_date: datetime.datetime