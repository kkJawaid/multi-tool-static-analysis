from fastapi import FastAPI 
from app.routers import user_profile_router 
from app.routers import user_auth_router 
from app.routers import blog_router
from app.routers import bookmark_router
from app.routers import comment_router

app = FastAPI(title="Multi Tool Static Analysis on an Intentionally Vulnerable Blog API")

app.include_router(user_auth_router.router)
app.include_router(user_profile_router.router)
app.include_router(blog_router.router)
app.include_router(bookmark_router.router)
app.include_router(comment_router.router)

@app.get("/")
def landing():
    return {"Hello from my vulnerable blog API"}
