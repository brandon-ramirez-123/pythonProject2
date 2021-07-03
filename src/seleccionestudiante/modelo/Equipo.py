from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.seleccionestudiante.modelo.declarative_base import Base


class Equipo(Base):
    __tablename__ = "equipo"
    idEquipo = Column(Integer, primary_key=True)
    denominacionEquipo = Column(String)
