from pydantic import BaseModel, EmailStr, Field
from typing import Optional 

class UpdateUserRequest(BaseModel):
    username: Optional[str] = Field(default = None, min_length=5)
    email: Optional[EmailStr] = Field(default = None)
    password: Optional[str] = Field(default = None, min_length=8)