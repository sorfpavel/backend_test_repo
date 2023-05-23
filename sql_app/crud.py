# this file specifies the methods to operate with data

from sqlalchemy.orm import Session
from . import models, schemas

######## read methods ##############

def get_person_by_id(db: Session, person_id: int): # method to read person from database by id
    return db.query(models.Master).filter(models.Master.id == person_id).first()

def get_person_by_last_name(db: Session, last_name: str): # method to read person by last_name
    return db.query(models.Master).filter(models.Master.last_name == last_name).first()

def get_person_by_first_name(db: Session, first_name): # method to read person by first_name
    return db.query(models.Master).filter(models.Master.first_name == first_name).first()

def get_city_by_id(db: Session, city_id: int): # method to read city based on id
    return db.query(models.Mereni_data).filter(models.Mereni_data.id == city_id).first()

def get_city_by_user(db: Session, last_name): # method to read city specified for user (join of 2 tables)
    person_residence = db.query(models.Mereni_data).join(models.Master).filter(models.Master.last_name == last_name).first()
    return person_residence.bydliste

########### methods to create data ###############

def create_person(db: Session, person: schemas.MasterCreate):
    db_person = models.Master(first_name = person.first_name, last_name = person.last_name, ref_bydliste = person.ref_bydliste)
    db.add(db_person)   
    db.commit()
    db.refresh(db_person)
    return db_person

# upgrade should be defing these functions in classes and call them as instances in main