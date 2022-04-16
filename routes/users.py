# Python
from typing import List

# Models
from models.User import User, UserLogin

# FastAPI
from fastapi import status, APIRouter

router = APIRouter()

@router.get(
    path="/",
    status_code=status.HTTP_200_OK,
    response_model=List[User],
    summary="Show all users",
    tags=['Users'])
def show_all(user: User):
    pass

@router.get(
    path="/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a user",
    tags=['Users'])
def show_user(user: UserLogin):
    pass

@router.delete(
    path="/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a user",
    tags=['Users'])
def delete_user(user: UserLogin):
    pass

@router.put(
    path="/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a user",
    tags=['Users'])
def update_user(user: UserLogin):
    pass