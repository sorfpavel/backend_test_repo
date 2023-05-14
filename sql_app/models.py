from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Master(Base):
    __tablename__ = "master"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    ref_bydliste = Column(Integer)

    relation1 = relationship("Mereni_data", back_populates="relation2")

class Mereni_data(Base):
    __tablename__ = "mereni_data"

    id = Column(Integer, ForeignKey("master.ref_bydliste"), primary_key=True, index=True)
    bydliste = Column(String)

    relation2 = relationship("Master", back_populates="relation1")
    