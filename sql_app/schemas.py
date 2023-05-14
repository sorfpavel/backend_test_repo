from pydantic import BaseModel

class MasterBase(BaseModel): # used as base class fof inheriting common atributes
    first_name: str
    last_name: str

class MasterCreate(MasterBase): # used for creating a record
    pass

class MasterRead(MasterBase): # usef for reading data from database via API
    id: int

    class Config: # declare that we are using ORM models and accesing data not only from dictionary
        orm_mode = True


class MereniDataBase(BaseModel): # used as base class for inheriting common atributes
    ref_master: int
    bydliste: str



class MereniDataCreate(MereniDataBase): # used for creating a record
    pass

class MereniDataRead(MereniDataBase): # used for reading data from database via API
    id: int

    

    class Config: # declare that we are using ORM models and accesing data not only from dictionary
        orm_mode = True

        