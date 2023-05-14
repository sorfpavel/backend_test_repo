from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Master(Base):
    __tablename__ = "master"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)

    relation1 = relationship("Mereni_data", back_populates="relation2")

class Mereni_data(Base):
    __tablename__ = "mereni_data"

    id = Column(Integer, primary_key=True, index=True)
    ref_master = Column(Integer, ForeignKey("master.id"))
    bydliste = Column(String)

    relation2 = relationship("Master", back_populates="relation1")
    