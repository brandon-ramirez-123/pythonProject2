from datetime import datetime
from src.seleccionestudiante.modelo.Estudiante import Estudiante
from src.seleccionestudiante.modelo.Actividad import Actividad
from src.seleccionestudiante.modelo.Asignatura import Asignatura
from src.seleccionestudiante.modelo.Equipo import Equipo
from src.seleccionestudiante.modelo.declarative_base import Session, engine, Base


def anade_registros():
    # Crea la base de datos
    Base.metadata.create_all(engine)

    # Abre sesión
    session = Session()

    # Crea estudiantes
    estudiante1 = Estudiante(apellidoPaterno="Ramos", apellidoMaterno="Ortega", nombres="Juan Carlos",
                             elegible=True)
    estudiante2 = Estudiante(apellidoPaterno="Solis", apellidoMaterno="Matos", nombres="Pedro",
                             elegible=True)
    estudiante3 = Estudiante(apellidoPaterno="Paredes", apellidoMaterno="Torres", nombres="Luis Alberto",
                             elegible=True)
    estudiante4 = Estudiante(apellidoPaterno="Garcia", apellidoMaterno="Mateo", nombres="Miguel Angel",
                             elegible=True)

    session.add(estudiante1)
    session.add(estudiante2)
    session.add(estudiante3)
    session.add(estudiante4)
    session.commit()

    # crear asignatura
    asignatura1 = Asignatura(nombreAsignatura="Análisis y diseño de sistemas")
    asignatura2 = Asignatura(nombreAsignatura="Pruebas de software")
    session.add(asignatura1)
    session.add(asignatura2)
    session.commit()

    # crear equipo de trabajo
    equipo1 = Equipo(denominacionEquipo="Equipo01")
    equipo2 = Equipo(denominacionEquipo="Equipo02")
    session.add(equipo1)
    session.add(equipo2)
    session.commit()

    # crear actividad
    actividad1 = Actividad(denominacionActividad="Prueba unitaria", fecha=datetime(2021, 9, 28, 00, 00, 00, 00000))
    actividad2 = Actividad(denominacionActividad="TDD", fecha=datetime(2021, 9, 25, 00, 00, 00, 00000))
    actividad3 = Actividad(denominacionActividad="BDD", fecha=datetime(2021, 9, 25, 00, 00, 00, 00000))
    session.add(actividad1)
    session.add(actividad2)
    session.add(actividad3)
    session.commit()

    # relacionar equipo con actividad
    equipo1.actividades = [actividad1, actividad2]
    equipo2.actividades = [actividad3]
    session.commit()

    # Relacionar Asignatura con estudiantes
    asignatura1.estudiantes = [estudiante1, estudiante4]
    asignatura2.estudiantes = [estudiante2, estudiante3]
    session.commit()

    # Relacionar equipo con estudiantes
    equipo1.estudiantes = [estudiante1, estudiante3]
    equipo2.estudiantes = [estudiante2, estudiante4]
    session.commit()

    session.close()


def eliminar_registros():
    session = Session()

    estudiantes = session.query(Estudiante).all()
    for estudiante in estudiantes:
        session.delete(estudiante)
    session.commit()
    session.close()

    asignaturas = session.query(Asignatura).all()
    for asignatura in asignaturas:
        session.delete(asignatura)
    session.commit()
    session.close()

    actividades = session.query(Actividad).all()
    for actividad in actividades:
        session.delete(actividad)
    session.commit()
    session.close()

    equipos = session.query(Equipo).all()
    for equipo in equipos:
        session.delete(equipo)
    session.commit()
    session.close()


if __name__ == '__main__':
    while True:
        print("0 Salir")
        print("1 Añadir registros")
        print("2 Eliminar registros")
        opcion = int(input("Opción: "))

        if opcion == 0:
            print("Fin...")
            break
        elif opcion == 1:
            anade_registros()
            print("Registros añadidos")
        elif opcion == 2:
            eliminar_registros()
            print("Registros eliminados")
        else:
            print("Opción incorrecta")
        print("\n\n\n")
