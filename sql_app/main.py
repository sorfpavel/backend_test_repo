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

# path method to return city by id

@app.get("/city/{city_id}", response_model=schemas.MereniData)
def read_city_by_id(city_id:int, db: Session = Depends(get_db)):
    city = crud.get_city_by_id(db, city_id=city_id)
    if city is None:
        raise HTTPException(status_code=404, detail = "Id not found")
    return city


# @app.post("/person/", response_model=schemas.Master)
# def create_person(person: schemas.MasterCreate, db: Session = Depends(get_db)):
#     db_person = crud.create_person(db, last_name = person.last_name)
#     if db_person:
#         raise HTTPException(status_code=200,detail="User succesfully created.")
#     return db_person