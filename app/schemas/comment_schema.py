from pydantic import BaseModel, Field 

class CreateCommentRequest(BaseModel):
    commentText: str = Field(min_length = 1)