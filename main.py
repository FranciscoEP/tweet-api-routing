# Python
from typing import List

# Models

from models.Tweet import Tweet

# FastAPI
from fastapi import FastAPI
from routes import router


app = FastAPI()

app.include_router(router.api_router)