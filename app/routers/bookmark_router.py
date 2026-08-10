from fastapi import APIRouter, Depends
from app.dependencies.auth import get_current_user
from app.controllers.bookmark_controller import (create_bookmark_controller, delete_bookmark_controller)

router = APIRouter(prefix="/bookmarks", tags=["Bookmarks"])

# to create public bookmarks
@router.post("/add/{blogId}")
def create_bookmark_router(blogId: int, user: dict = Depends(get_current_user)):
    return create_bookmark_controller(blogId, user["user_id"])

# to delete publc bookmarks
@router.delete("/{blogId}")
def delete_bookmark_router(blogId: int, user: dict = Depends(get_current_user)):
    return delete_bookmark_controller(blogId, user["user_id"])

