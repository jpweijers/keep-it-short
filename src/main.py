from fastapi import FastAPI

from src import schemas

app = FastAPI()


@app.get("/")
def read_root():
    return "Welcome to Keep it Short"


@app.post("/url")
def create_url(url: schemas.URLBase):
    return f"TODO: Create database entry for: {url.target_url}"
