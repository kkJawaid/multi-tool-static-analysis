from fastapi import APIRouter
from app.schemas.user_auth_schema import ( RegistrationRequest, LoginRequest )
from app.controllers.user_auth_controller import ( register_user, login_user )

router = APIRouter(prefix="/auth", tags=["Authentication Flow"])

@router.post("/registration")
def user_registration(user: RegistrationRequest):
    return register_user(user)

@router.post("/login")
def user_login(user: LoginRequest):
    return login_user(user)