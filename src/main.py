import secrets

# import validators
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import models, schemas
from .database import get_db, engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return "Welcome to Keep it Short"


@app.post("/url", response_model=schemas.URLInfo)
def create_url(url: schemas.URLBase, db: Session = Depends(get_db)):
    chars = "ABCDFGHIJKLMNOPQRSTUVWXYZ"
    key = "".join(secrets.choice(chars) for _ in range(5))
    secret_key = "".join(secrets.choice(chars) for _ in range(8))
    db_url = models.URL(target_url=url.target_url, key=key, secret_key=secret_key)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    db_url.url = key
    db_url.admin_url = secret_key

    return db_url
