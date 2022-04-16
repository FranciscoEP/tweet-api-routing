# Python
from typing import List

# FastAPI
from fastapi import FastAPI
from routes import router


app = FastAPI()


app.include_router(router.api_router)