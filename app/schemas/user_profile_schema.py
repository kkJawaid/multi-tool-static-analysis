from pydantic import BaseModel, EmailStr, Field

class RegisterUser(BaseModel):
    username: str = Field(min_length=5)
    email: EmailStr
    password: str = Field(min_length=8)