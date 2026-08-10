from fastapi import APIRouter, Depends
from app.controllers.blog_controller import ( fetch_all_blogs, fetch_specific_blog, search_blog, fetch_comments, create_blog_function, edit_blog_function, delete_blog_function)
from app.dependencies.auth import get_current_user
from app.schemas.blog_schema import ( CreateBlogRequest, UpdateBlogRequest )

router = APIRouter(prefix="/blog", tags=["Blogs"])

# to retrieve all blogs
@router.get("/")
def get_all_blogs():
    return fetch_all_blogs()

# to retrieve specific blog
@router.get("/{blogId}")
def get_specific_blog(blogId: int):
    return fetch_specific_blog(blogId)

# to search for specific blog
@router.get("/search/")
def search_specific_blog(search: str = 'a'):
    return search_blog(search)

# to get all comments of blog
@router.get("/{blogId}/comments")
def get_blog_comments(blogId: int):
    return fetch_comments(blogId)

# to create blog
@router.post("/")
def create_blog(blog: CreateBlogRequest, current_user: dict = Depends(get_current_user)):
    return create_blog_function(current_user["user_id"], blog)

# to edit blog
@router.patch("/{blogId}")
def edit_blog(blog: UpdateBlogRequest, blogId: int, current_user: dict = Depends(get_current_user)):
    blog = blog.model_dump(exclude_unset=True)
    return edit_blog_function(current_user["user_id"], blogId, blog)

# to delete blog 
@router.delete("/{blogId}")
def delete_blog( blogId: int, current_user: dict = Depends(get_current_user)):
    return delete_blog_function(current_user["user_id"], blogId)