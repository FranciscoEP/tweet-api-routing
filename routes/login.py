# Python
from typing import List

# Models
from models.User import User, UserLogin
from fastapi import status
from fastapi import APIRouter

router = APIRouter()

@router.get(path="/")
def home():
    return {"Twitter API": "Working"}

@router.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
    tags=['login'])
def signup(user: UserLogin):
    pass

@router.post(
    path="/login",
    status_code=status.HTTP_200_OK,
    response_model=User,
    summary="Login a user",
    tags=['login'])
def Login(user: UserLogin):
    pass