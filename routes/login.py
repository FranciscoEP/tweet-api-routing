# Python
from typing import List
import json
# Models
from models.Tweet import Tweet
from models.User import User, UserLogin, UserRegister

from fastapi import status
from fastapi import APIRouter
from fastapi import Body

router = APIRouter()

@router.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
    tags=['login'])
def signup(user: UserRegister = Body(...)):
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
    with open("users.json", "r+", encoding="UTF-8") as f:
        results = json.loads(f.read())
        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user

@router.post(
    path="/login",
    status_code=status.HTTP_200_OK,
    response_model=User,
    summary="Login a user",
    tags=['login'])
def Login(user: UserLogin):
    pass