from typing import TypeAlias, TypedDict


Estudiante: TypeAlias = dict[str, float]
Reporte: TypeAlias = dict[str, Estudiante]


class EstadisticasTarea(TypedDict):
    mayor: float
    mejor: str
    menor: float
    peor: str
    promedio: float
    cantidad: int
    total: float


def calcular_estadisticas_tarea(reporte: Reporte, tarea: str) -> EstadisticasTarea:
    """
    Calcula estadísticas de una tarea específica a partir de las notas de los estudiantes.

    Parámetros:
        reporte (Reporte): Diccionario de diccionarios con
            los nombres de los estudiantes como llaves y sus tareas con notas como valores.
        nombre_tarea (str): Nombre de la tarea a analizar.

    Retorna:
        EstadisticasTarea: Diccionario con las estadísticas de la tarea:
            - "mayor": La nota más alta obtenida.
            - "mejor": Nombre del estudiante con la nota más alta.
            - "menor": La nota más baja obtenida.
            - "peor": Nombre del estudiante con la nota más baja.
            - "promedio": Promedio de las notas.
            - "cantidad": Número de estudiantes que realizaron la tarea.
            - "total": Suma de todas las notas.
    """
    notas: dict[str, float] = {
        estudiante: tareas[tarea]
        for estudiante, tareas in reporte.items()
        if tarea in tareas
    }

    total: int = int(sum(notas.values()))
    cantidad: int = len(notas)
    mejor: str = max(notas, key=lambda e: notas[e])
    peor: str = min(notas, key=lambda e: notas[e])

    estadisticasTarea: EstadisticasTarea = {
        "mayor": notas[mejor],
        "mejor": mejor,
        "menor": notas[peor],
        "peor": peor,
        "promedio": total / cantidad,
        "cantidad": cantidad,
        "total": total,
    }

    return estadisticasTarea


def test_estadisticas_basicas():
    estudiantes: Reporte = {
        "Roberto": {"Tarea 1": 80, "Tarea 2": 90},
        "Maria": {"Tarea 1": 60, "Tarea 2": 70},
        "Juan": {"Tarea 1": 100},
    }
    resultado = calcular_estadisticas_tarea(estudiantes, "Tarea 1")
    assert resultado["mayor"] == 100
    assert resultado["mejor"] == "Juan"
    assert resultado["menor"] == 60
    assert resultado["peor"] == "Maria"
    assert resultado["promedio"] == 80.0
    assert resultado["cantidad"] == 3
    assert resultado["total"] == 240
    print("Caso 1: Estadísticas básicas calculadas correctamente")


def test_tarea_no_realizada_por_todos():
    estudiantes: Reporte = {
        "Roberto": {"Tarea 1": 80, "Tarea 2": 90},
        "Maria": {"Tarea 1": 60},
        "Juan": {"Tarea 2": 50},
    }
    resultado = calcular_estadisticas_tarea(estudiantes, "Tarea 2")
    assert resultado["cantidad"] == 2
    assert resultado["mejor"] == "Roberto"
    assert resultado["peor"] == "Juan"
    assert resultado["total"] == 140
    assert resultado["promedio"] == 70.0
    print("Caso 2: Solo considera estudiantes que realizaron la tarea")


def test_un_solo_estudiante():
    estudiantes: Reporte = {
        "Ana": {"Tarea 1": 75},
    }
    resultado = calcular_estadisticas_tarea(estudiantes, "Tarea 1")
    assert resultado["mayor"] == 75
    assert resultado["menor"] == 75
    assert resultado["mejor"] == "Ana"
    assert resultado["peor"] == "Ana"
    assert resultado["cantidad"] == 1
    assert resultado["promedio"] == 75.0
    print("Caso 3: Un solo estudiante manejado correctamente")


if __name__ == "__main__":
    tests = [
        test_estadisticas_basicas,
        test_tarea_no_realizada_por_todos,
        test_un_solo_estudiante,
    ]
    passed = 0
    failed = 0
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"FAILED: {test.__name__} - {e}")
            failed += 1
    print("-----------------------")
    print(f"Passed: {passed} | Failed: {failed}")
