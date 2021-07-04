from sqlalchemy import Column, Integer, String, Date, ForeignKey
from .declarative_base import Base


class Actividad(Base):
    __tablename__ = "actividad"
    idActividad = Column(Integer, primary_key=True)
    denominacionActividad = Column(String)
    fecha = Column(Date)

    equipo = Column(Integer, ForeignKey("equipo.idEquipo"))
