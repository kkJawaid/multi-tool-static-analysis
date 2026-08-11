from pydantic import BaseModel, EmailStr, Field
from typing import Optional 

class UpdateUserRequest(BaseModel):
    user_name: Optional[str] = Field(default = None, min_length=5)
    user_email: Optional[EmailStr] = Field(default = None)
    user_password: Optional[str] = Field(default = None, min_length=8)