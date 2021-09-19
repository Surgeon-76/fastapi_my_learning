from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models,schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/customers/", response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
#     db_customer = crud.get_customer_by_email(db, email=customer.email)
#     if db_customer:
#         raise HTTPException(status_code=400, detail="Email уже зарегестрирован")
    return crud.create_customer(db=db, customer=customer)
