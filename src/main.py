# import validators
from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import engine, get_db

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return "Welcome to Keep it Short"


@app.post("/url", response_model=schemas.URLInfo)
def create_url(url: schemas.URLBase, db: Session = Depends(get_db)):
    db_url = crud.create_db_url(db=db, url=url)
    db_url.url = db_url.key
    db_url.admin_url = db_url.secret_key

    return db_url


@app.get("/{url_key}")
def forward_to_target_url(
    url_key: str, request: Request, db: Session = Depends(get_db)
):
    if db_url := crud.get_db_url_by_key(db=db, url_key=url_key):
        return RedirectResponse(db_url.target_url)
    else:
        message = f"URL '{request.url}' doesn't exist."
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)
