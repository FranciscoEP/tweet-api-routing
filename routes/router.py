from fastapi import APIRouter

from routes import users, login, tweets

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(tweets.router, prefix="/tweets", tags=["Tweets"])