# Python
from typing import List

# Models
from models.Tweet import Tweet
from models.User import User, UserLogin, UserRegister
from fastapi import status
from fastapi import APIRouter

router = APIRouter()

@router.post(
    path="/signup",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
    tags=['login'])
def signup(tweet: Tweet):
    """
    Signup a new user
    This path operation register a new user in the app.

    Parameters:
        - Request body parameter
            - user: UserRegister

    Returns a JSON with the basic user information
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: Optional[date]
        - created_at: date
        - updated_at: date
    """

    pass

@router.post(
    path="/login",
    status_code=status.HTTP_200_OK,
    response_model=User,
    summary="Login a user",
    tags=['login'])
def Login(user: UserLogin):
    pass