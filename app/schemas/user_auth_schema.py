from pydantic import BaseModel, EmailStr, Field

class RegistrationRequest(BaseModel):
    username: str = Field(min_length=5)
    email: EmailStr
    password: str = Field(min_length=8)

class LoginRequest(BaseModel):
    email: EmailStr
    password: str= Field(min_length=8)