from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.seleccionestudiante.modelo.declarative_base import Base


class Asignatura(Base):
    __tablename__ = "asignatura"
    idAsignatura = Column(Integer, primary_key=True)
    nombreAsignatura = Column(String)
