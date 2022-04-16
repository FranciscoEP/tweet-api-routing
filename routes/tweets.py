# Python
from typing import List
import json
# Models
from models.Tweet import Tweet

# FastAPI
from fastapi import status, APIRouter, Body

router = APIRouter()

@router.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all tweets",
    tags=['Tweets']
    )
def get_all_tweets():
    '''    
    Show all tweets 
    
    This path operation show all tweets in the app.

    Parameters:
        - Request body parameter
            - tweet: Tweet

    Returns a JSON List with the basic tweet information
        - tweet_id: UUID
        - content: str
        - created_at: date
        - updated_at: date
    '''
    with open("tweets.json", "r+", encoding="UTF-8") as f:
        results = json.loads(f.read())
        print(results)
        return results

@router.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a tweet",
    tags=['Tweets'])
def post_tweet(tweet: Tweet =Body(...)):
    """
    Signup a new user
    This path operation post a tweet in the app.

    Parameters:
        - Request body parameter
            - tweet: Tweet

    Returns a JSON with the basic tweet information
        - tweet_id: UUID
        - content: str
        - created_at: datetime
        - updated_at: Optional[datetime]
        - by: User
    """
    with open("tweets.json", "r+", encoding="UTF-8") as f:
        results = json.loads(f.read())
        tweet_dict = tweet.dict()
        tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
        tweet_dict["created_at"] = str(tweet_dict["created_at"])
        tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"])
        tweet_dict["by"]["birth_date"] = str(tweet_dict["by"]["birth_date"])

        if tweet_dict["updated_at"]:
            tweet_dict["updated_at"] = str(tweet_dict["updated_at"])

        results.append(tweet_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return tweet

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