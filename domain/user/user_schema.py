from pydantic import BaseModel, field_validator, EmailStr
from pydantic_core.core_schema import FieldValidationInfo


class UserCreate(BaseModel):
    username: str
    password1: str
    password2: str
    email: EmailStr
    
    @field_validator("username","password1", "password2", "email")
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("NOT_ALLOW_EMPTY_VALUE")
        return v
    
    @field_validator("password2")
    def passwords_match(cls, v, info: FieldValidationInfo):
        if "password1" in info.data and v != info.data["password1"]:
            raise ValueError("PASSWORD_NOT_MATCH")
        return v