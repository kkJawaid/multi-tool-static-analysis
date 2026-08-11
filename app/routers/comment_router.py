from fastapi import APIRouter, Depends
from app.dependencies.auth import get_current_user
from app.controllers.comment_controller import (create_comment_controller, update_comment_controller, delete_comment_controller, find_related_comments_controller)
from app.schemas.comment_schema import (CreateCommentRequest)

router = APIRouter(prefix="/comments", tags=["Comments"])

@router.post("/{blogId}")
def create_comment_router(blogId: int, comment: CreateCommentRequest, current_user: dict = Depends(get_current_user)):
    return create_comment_controller(current_user["user_id"], blogId, comment)

@router.patch("/{blogId}/{commentId}")
def update_comment_router(blogId: int, commentId:int, comment: CreateCommentRequest, current_user: dict = Depends(get_current_user)):
    # comment = comment.model_dump(excluse_unset = True)
    return update_comment_controller( blogId, comment, commentId)

@router.delete("/{blogId}/{commentId}")
def delete_comment_router(blogId: int, commentId: int, current_user: dict = Depends(get_current_user)):
    return delete_comment_controller( blogId, commentId)

# intentionally vulnerable
@router.get("/{commentId}")
def find_related_comments_router(commentId: int):
    return find_related_comments_controller(commentId)