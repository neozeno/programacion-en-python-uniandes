from typing import TypeAlias

Matriz: TypeAlias = list[list[int]]


def promedio_fila(matriz: Matriz, fila: int) -> float:
    """
    Calcula el promedio de las notas de una fila del salón.

    Los valores 0 en la matriz indican asientos vacíos y no se
    incluyen en el cálculo del promedio.

    Parámetros:
        matriz (Matriz): Matriz que representa el salón de clases.
        fila (int): Número de fila a calcular (la primera fila es la número 1).

    Retorna:
        float: Promedio de la fila redondeado a dos decimales.
               -1 si el número de fila no es válido.
               0 si la fila no tiene estudiantes.

    Ejemplos:
        >>> promedio_fila([[80, 90, 0], [70, 60, 50]], 1)
        85.0
        >>> promedio_fila([[80, 90, 0], [70, 60, 50]], 3)
        -1
        >>> promedio_fila([[0, 0, 0]], 1)
        0
    """
    if fila < 1 or fila > len(matriz):
        return -1

    estudiantes: list[int] = [nota for nota in matriz[fila - 1] if nota != 0]

    if len(estudiantes) == 0:
        return 0

    return round(sum(estudiantes) / len(estudiantes), 2)


def test_fila_valida():
    matriz: Matriz = [[80, 90, 0], [70, 60, 50]]
    assert promedio_fila(matriz, 1) == 85.0
    print("Caso 1: Promedio de fila válida calculado correctamente")


def test_fila_invalida_mayor():
    matriz: Matriz = [[80, 90], [70, 60]]
    assert promedio_fila(matriz, 3) == -1
    print("Caso 2: Fila mayor al tamaño retorna -1")


def test_fila_invalida_menor():
    matriz: Matriz = [[80, 90], [70, 60]]
    assert promedio_fila(matriz, 0) == -1
    print("Caso 3: Fila 0 retorna -1")


def test_fila_sin_estudiantes():
    matriz: Matriz = [[0, 0, 0], [70, 60, 50]]
    assert promedio_fila(matriz, 1) == 0
    print("Caso 4: Fila sin estudiantes retorna 0")


def test_fila_con_todos_los_estudiantes():
    matriz: Matriz = [[100, 90, 80]]
    assert promedio_fila(matriz, 1) == 90.0
    print("Caso 5: Fila completa calculada correctamente")


def test_redondeo():
    matriz: Matriz = [[100, 90, 85]]
    assert promedio_fila(matriz, 1) == 91.67
    print("Caso 6: Promedio redondeado a dos decimales correctamente")


if __name__ == "__main__":
    tests = [
        test_fila_valida,
        test_fila_invalida_mayor,
        test_fila_invalida_menor,
        test_fila_sin_estudiantes,
        test_fila_con_todos_los_estudiantes,
        test_redondeo,
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
