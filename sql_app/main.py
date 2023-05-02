from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas

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


# Defining path methods

@app.get("/person/{person_id}", response_model=schemas.Master)
def read_person_by_id(person_id: int, db: Session = Depends(get_db)):
    person = crud.get_person_by_id(db, person_id = person_id)
    if person_id is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return person