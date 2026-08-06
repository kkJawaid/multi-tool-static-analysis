from datetime import datetime, timedelta
from jose import jwt
from dotenv import load_dotenv
load_dotenv()
import os

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 240

def create_access_token(data: dict):
    payload = data.copy()
    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    payload["exp"] = expire
    return jwt.encode(
        payload,
        os.getenv("SECRET_KEY"),
        algorithm=ALGORITHM
    )





