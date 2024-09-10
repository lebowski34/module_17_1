from fastapi import FastAPI
from app.models import user, task


app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}
