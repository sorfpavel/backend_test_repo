# defining methods to ineract with database (Create, Read, Update, Delete)

from sqlalchemy.orm import Session

from . import models, schemas

# defining methods to: read a user by last name, first name

def get_person_by_id(db: Session, person_id: int):
    return db.query(models.Master).filter(models.Master.id == person_id).first()

def get_person_by_last_name(db: Session, last_name: str):
    return db.query(models.Master).filter(models.Master.last_name == last_name).first()

def get_person_by_first_name(db: Session, first_name):
    return db.query(models.Master).filter(models.Master.first_name == first_name).first()

# now define methotds to create and save data

def create_person(db: Session, person:schemas.MasterCreate):
    db_person = models.Master
    db.add(db_person)   
    db.commit()
    db.refresh(db_person)

