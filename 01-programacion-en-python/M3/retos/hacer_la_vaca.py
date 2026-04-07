from typing import TypeAlias

Salon: TypeAlias = list[list[int]]

PRECIOS: dict[str, int] = {
    "botella": 120_000,
    "pastel": 35_000,
}


def encontrar_mayor_aportante(salon: Salon) -> tuple[int, int, int]:
    """
    Encuentra el estudiante que más dinero aportó y su posición en el salón.

    Parámetros:
        salon (Salon): Matriz con los aportes de cada estudiante.

    Retorna:
        tuple[int, int, int]: (monto_mayor, fila, columna) del mayor aportante.
    """
    mayor_aporte: int = 0
    fila_mayor_aportante: int = 0
    columna_mayor_aportante: int = 0

    for x in range(len(salon)):
        for y in range(len(salon[x])):
            if salon[x][y] > mayor_aporte:
                mayor_aporte = salon[x][y]
                fila_mayor_aportante = x
                columna_mayor_aportante = y

    return mayor_aporte, fila_mayor_aportante, columna_mayor_aportante


def hacer_la_vaca(salon: Salon, vaca: str) -> list[str | int]:
    """
    Determina si el dinero recolectado alcanza para el regalo y quién fue
    el mayor aportante.

    Parámetros:
        salon (Salon): Matriz que representa el salón. Cada valor
            es el aporte en pesos del estudiante en esa posición.
        vaca (str): Tipo de regalo, puede ser 'botella' o 'pastel'.

    Retorna:
        list[str | int]: Lista con tres elementos:
            - [0]: 'Hay Vaca' si el total alcanza, 'No Alcanza' de lo contrario.
            - [1]: Fila del estudiante que más aportó.
            - [2]: Columna del estudiante que más aportó.

    Ejemplos:
        >>> hacer_la_vaca([[10_000, 20_000], [50_000, 5_000]], 'pastel')
        ['Hay Vaca', 1, 0]
    """
    total: int = sum(
        salon[x][y] for x in range(len(salon)) for y in range(len(salon[x]))
    )
    precio: int = PRECIOS[vaca]
    mensaje: str = "Hay Vaca" if total >= precio else "No Alcanza"

    _, fila, columna = encontrar_mayor_aportante(salon)

    return [mensaje, fila, columna]


def test_hay_vaca_pastel():
    salon: list[list[int]] = [
        [10_000, 20_000],
        [50_000, 5_000],
    ]
    resultado = hacer_la_vaca(salon, "pastel")
    assert resultado[0] == "Hay Vaca"
    assert resultado[1] == 1
    assert resultado[2] == 0
    print("Caso 1: Alcanza para el pastel, identifica mayor aportante")


def test_no_alcanza_botella():
    salon: list[list[int]] = [
        [5_000, 10_000],
        [8_000, 7_000],
    ]
    resultado = hacer_la_vaca(salon, "botella")
    assert resultado[0] == "No Alcanza"
    assert resultado[1] == 0
    assert resultado[2] == 1
    print("Caso 2: No alcanza para la botella, identifica mayor aportante")


def test_hay_vaca_botella():
    salon: list[list[int]] = [
        [50_000, 30_000, 20_000],
        [10_000, 15_000, 25_000],
    ]
    resultado = hacer_la_vaca(salon, "botella")
    assert resultado[0] == "Hay Vaca"
    assert resultado[1] == 0
    assert resultado[2] == 0
    print("Caso 3: Alcanza para la botella, identifica mayor aportante")


def test_un_solo_estudiante():
    salon: list[list[int]] = [[40_000]]
    resultado = hacer_la_vaca(salon, "pastel")
    assert resultado[0] == "Hay Vaca"
    assert resultado[1] == 0
    assert resultado[2] == 0
    print("Caso 4: Un solo estudiante manejado correctamente")


if __name__ == "__main__":
    tests = [
        test_hay_vaca_pastel,
        test_no_alcanza_botella,
        test_hay_vaca_botella,
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
