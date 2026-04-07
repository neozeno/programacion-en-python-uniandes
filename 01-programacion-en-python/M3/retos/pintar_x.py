from typing import TypeAlias

Matriz: TypeAlias = list[list[int | float]]


def aplicar_operacion(valor: int | float, operacion: str) -> int | float:
    """
    Aplica una operación aritmética a un valor usando el mismo valor como operando.

    Parámetros:
        valor (int | float): Valor de la casilla.
        operacion (str): Operación a aplicar ('+', '-', '*', '/').

    Retorna:
        int | float: Resultado de la operación.

    Ejemplos:
        >>> aplicar_operacion(5, '+')
        10
        >>> aplicar_operacion(5, '-')
        0
        >>> aplicar_operacion(5, '*')
        25
        >>> aplicar_operacion(5, '/')
        1.0
    """
    if operacion == "+":
        return valor + valor
    elif operacion == "-":
        return valor - valor
    elif operacion == "*":
        return valor * valor
    else:
        return valor / valor


def pintar_x(matriz: Matriz, operacion: str) -> Matriz:
    """
    Aplica una operación aritmética sobre todas las casillas que forman
    la X (ambas diagonales) de una matriz cuadrada.

    Parámetros:
        matriz (Matriz): Matriz cuadrada con números positivos.
        operacion (str): Operación a aplicar ('+', '-', '*', '/').

    Retorna:
        Matriz: Matriz modificada con la X repintada.

    Ejemplos:
        >>> pintar_x([[1, 2, 3], [4, 5, 6], [7, 8, 9]], '+')
        [[2, 2, 6], [4, 10, 6], [14, 8, 18]]
    """
    n: int = len(matriz)

    for i in range(n):
        matriz[i][i] = aplicar_operacion(matriz[i][i], operacion)
        j: int = n - 1 - i
        if j != i:
            matriz[i][j] = aplicar_operacion(matriz[i][j], operacion)

    return matriz


def test_suma():
    matriz: Matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    resultado = pintar_x(matriz, "+")
    assert resultado == [[2, 2, 6], [4, 10, 6], [14, 8, 18]]
    print("Caso 1: Suma aplicada correctamente")


def test_resta():
    matriz: Matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    resultado = pintar_x(matriz, "-")
    assert resultado == [[0, 2, 0], [4, 0, 6], [0, 8, 0]]
    print("Caso 2: Resta aplicada correctamente")


def test_multiplicacion():
    matriz: Matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    resultado = pintar_x(matriz, "*")
    assert resultado == [[1, 2, 9], [4, 25, 6], [49, 8, 81]]
    print("Caso 3: Multiplicación aplicada correctamente")


def test_division():
    matriz: Matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    resultado = pintar_x(matriz, "/")
    assert resultado == [[1.0, 2, 1.0], [4, 1.0, 6], [1.0, 8, 1.0]]
    print("Caso 4: División aplicada correctamente")


def test_matriz_4x4():
    matriz: Matriz = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    resultado = pintar_x(matriz, "+")
    assert resultado[0][0] == 2
    assert resultado[0][3] == 8
    assert resultado[1][1] == 12
    assert resultado[1][2] == 14
    assert resultado[2][2] == 22
    assert resultado[3][0] == 26
    assert resultado[3][3] == 32
    assert resultado[0][1] == 2
    print("Caso 5: Matriz 4x4 procesada correctamente")


if __name__ == "__main__":
    tests = [test_suma, test_resta, test_multiplicacion, test_division, test_matriz_4x4]
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
