from fastapi import APIRouter

router = APIRouter(prefix="/profile", tags=["Users"])

# to get all user's details
@router.get("/")
def get_profile_details():
    return "to be implemented"

# to get user blogs that they've written
@router.get("/blogs")
def get_user_blogs():
    return "to be implemented"

# to get all the comments user has made
@router.get("/comments")
def get_user_comments():
    return "to be implemented"

# to get blogs user has bookmarked
@router.get("/bookmarks")
def get_user_bookmarks():
    return "to be implemented"

# to delete profile :(
@router.delete("/")
def delete_user_profile():
    return "to be implemented"

# to update user profile (username, pass, email)
@router.put("/")
def update_user_profile():
    return "to be implemented"


