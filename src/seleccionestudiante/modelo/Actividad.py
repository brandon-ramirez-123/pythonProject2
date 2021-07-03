from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from src.seleccionestudiante.modelo.declarative_base import Base


class Actividad(Base):
    __tablename__ = "actividad"
    idActividad = Column(Integer, primary_key=True)
    denominacionActividad = Column(String)
    Fecha = Column(Date)
