from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional

class BlogStatusEnum(str, Enum):
    public = "public",
    private = "private"

class CreateBlogRequest(BaseModel):
    title: str = Field(min_length= 5)
    text: str = Field(min_length= 100)
    status: BlogStatusEnum = BlogStatusEnum.public 


class UpdateBlogRequest(BaseModel):
    title: Optional[str] = Field(default = None , min_length= 2)
    text: Optional[str]  = Field(default = None, min_length= 100)
    status: Optional[BlogStatusEnum] = BlogStatusEnum.public 
