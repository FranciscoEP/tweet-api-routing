# FastAPI
from fastapi import FastAPI
from models.User import User
from models.Tweet import Tweet


app = FastAPI()

@app.get(path="/")
def home():
    return {"Twitter API": "Working"}