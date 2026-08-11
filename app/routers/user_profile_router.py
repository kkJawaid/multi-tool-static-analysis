from fastapi import APIRouter, Depends
from app.dependencies.auth import get_current_user
from app.controllers.user_profile_controller import ( profile_details, get_user_blogs_controller, get_user_comments_controller, get_user_bookmarks_controller, update_user_profile_controller, delete_user_profile_controller)
from app.schemas.user_profile_schema import (UpdateUserRequest)

router = APIRouter(prefix="/profile", tags=["Users"])

# to get all user's details
@router.get("/")
def get_profile_details(current_user: dict = Depends(get_current_user)):
    return profile_details(current_user["user_id"])

# to get user blogs that they've written
@router.get("/blogs")
def get_user_blogs(current_user: dict = Depends(get_current_user)):
    return get_user_blogs_controller(current_user["user_id"])

# to get all the comments user has made
@router.get("/comments")
def get_user_comments(current_user: dict = Depends(get_current_user)):
    return get_user_comments_controller(current_user["user_id"])

# to get blogs user has bookmarked
@router.get("/bookmarks")
def get_user_bookmarks(current_user: dict = Depends(get_current_user)):
    return get_user_bookmarks_controller(current_user["user_id"])

# to delete profile :(
@router.delete("/")
def delete_user_profile(current_user: dict = Depends(get_current_user)):
    return delete_user_profile_controller(current_user["user_id"])

# to update user profile (username, pass, email)
@router.patch("/")
def update_user_profile(user: UpdateUserRequest, current_user: dict = Depends(get_current_user)):
    user = user.model_dump(exclude_unset = True)
    return update_user_profile_controller(user, current_user["user_id"])


