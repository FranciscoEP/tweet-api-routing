# Python
from typing import List

# Models
from models.Tweet import Tweet

# FastAPI
from fastapi import status, APIRouter

router = APIRouter()

@router.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all tweets",
    tags=['Tweets']
    )
def get_all_tweets():
    return {"Twitter API": "Working"}

@router.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a tweet",
    tags=['Tweets'])
def post_tweet(tweet: Tweet):
    pass

@router.get(
    path="/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a tweet",
    tags=['Tweets'])
def get_tweet(tweet: Tweet):
    pass

@router.delete(
    path="/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a tweet",
    tags=['Tweets'])
def delete_tweet(tweet: Tweet):
    pass

@router.put(
    path="/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a tweet",
    tags=['Tweets'])
def update_tweet(tweet: Tweet):
    pass