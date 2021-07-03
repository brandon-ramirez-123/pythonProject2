from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from src.seleccionestudiante.modelo.declarative_base import Base


class Estudiante(Base):
    __tablename__ = "estudiante"
    idEstudiante = Column(Integer, primary_key=True)
    apellidoPaterno = Column(String)
    apellidoMaterno = Column(String)
    nombres = Column(String)
    elegible = Column(Boolean)
