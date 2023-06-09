from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI() # creating main app

# Dependency
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

# do samostatného souboru


# Defining path methods

@app.get("/person/{person_id}", response_model=schemas.MasterRead) # this method returns person by id
def read_person_by_id(person_id: int, db: Session = Depends(get_db)):
    person = crud.get_person_by_id(db, person_id = person_id)
    if person_id is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return person

@app.get("/city/{city_id}", response_model=schemas.MereniDataRead) # this method returns city by id (different table than first one)
def read_city_by_id(city_id:int, db: Session = Depends(get_db)):
    city = crud.get_city_by_id(db, city_id=city_id)
    if city is None:
        raise HTTPException(status_code=404, detail = "Id not found")
    return city

@app.get("/residence/{last_name}") # this method returns city based on users last_name
def read_city_by_person(last_name: str, db: Session = Depends(get_db)):
    city = crud.get_city_by_user(db, last_name=last_name)
    return city

@app.post("/person_create/", response_model=schemas.MasterCreate) # method to create new person in database
def create_person(person: schemas.MasterCreate, db: Session = Depends(get_db)):
    # should be condition to check if there is already the object
    return crud.create_person(db = db, person=person)