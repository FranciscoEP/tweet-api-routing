# Python
from typing import List
import json
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
def show_all():
    '''
    Show all users 
    
    This path operation show all users in the app.

    Parameters:
        - Request body parameter
            - user: UserRegister

    Returns a JSON List with the basic users information
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: Optional[date]
        - created_at: date
        - updated_at: date
    '''
    with open("users.json", "r+", encoding="UTF-8") as f:
        results = json.loads(f.read())
        return results

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