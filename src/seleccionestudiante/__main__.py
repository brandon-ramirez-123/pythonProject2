from datetime import datetime

from src.seleccionestudiante.modelo.Actividad import Actividad
from src.seleccionestudiante.modelo.Asignatura import Asignatura
from src.seleccionestudiante.modelo.Equipo import Equipo
from src.seleccionestudiante.modelo.Estudiante import Estudiante
from src.seleccionestudiante.modelo.declarative_base import Session, engine, Base

if __name__ == 'main':
    #   crea bd
    Base.metadata.create_all(engine)

    #   abre sesion
    session = Session()

    #   crea estudiantes
    estudiante1 = Estudiante(apellidoPaterno="apPat1",
                             apellidoMaterno="apMat1",
                             nombres="nomb1",
                             elegible=True);
    estudiante2 = Estudiante(apellidoPaterno="apPat2",
                             apellidoMaterno="apMat2",
                             nombres="nomb2",
                             elegible=True);
    estudiante3 = Estudiante(apellidoPaterno="apPat3",
                             apellidoMaterno="apMat3",
                             nombres="nomb3",
                             elegible=True);
    estudiante4 = Estudiante(apellidoPaterno="apPat4",
                             apellidoMaterno="apMat4",
                             nombres="nomb4",
                             elegible=True);
    session.add(estudiante1)
    session.add(estudiante2)
    session.add(estudiante3)
    session.add(estudiante4)
    session.commit()

    #   crea asignatura
    asignatura1 = Asignatura(nombreAsignatura="asignatura1")
    asignatura2 = Asignatura(nombreAsignatura="asignatura2")
    session.add(asignatura1)
    session.add(asignatura2)
    session.commit()

    #   crea equipo
    equipo1 = Equipo(denominacionEquipo="Equipo1")
    equipo2 = Equipo(denominacionEquipo="Equipo2")
    session.add(equipo1)
    session.add(equipo2)
    session.commit()

    #   crea actividad
    actividad1 = Actividad(denominacionActividad="Prueba unitaria", fecha=datetime(2021, 9, 28, 00, 00, 00, 00000))
    actividad2 = Actividad(denominacionActividad="TDD", fecha=datetime(2021, 9, 25, 00, 00, 00, 00000))
    actividad3 = Actividad(denominacionActividad="BDD", fecha=datetime(2021, 9, 23, 00, 00, 00, 00000))
    session.add(actividad1)
    session.add(actividad2)
    session.add(actividad3)
    session.commit()

    #   cierra
    session.close()
