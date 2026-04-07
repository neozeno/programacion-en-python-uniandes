def buscar_elemento(entrada: list[int], buscado: int) -> int:
    """
    Busca un número entero en una lista y retorna el índice de su primera aparición.

    Parámetros:
        entrada (list[int]): Lista en la que se buscará el número.
        buscado (int): Número entero a buscar.

    Retorna:
        int: Índice de la primera aparición del elemento, o -1 si no se encuentra.

    Ejemplos:
        >>> buscar_elemento([1, 2, 3, 4], 3)
        2
        >>> buscar_elemento([1, 2, 3, 2], 2)
        1
        >>> buscar_elemento([1, 2, 3], 9)
        -1
    """
    for i in range(len(entrada)):
        if entrada[i] == buscado:
            return i

    return -1


def test_encuentra_numero():
    assert buscar_elemento([1, 2, 3, 4], 3) != -1
    print("Caso 1: Encontró el número buscado")


def test_numero_no_encontrado():
    assert buscar_elemento([1, 2, 3, 4], 9) == -1
    print("Caso 2: Identificó que el número no se encontraba en la lista")


def test_posicion_correcta():
    assert buscar_elemento([10, 20, 30, 40], 30) == 2
    print("Caso 3: La posición del número encontrado es correcta")


def test_primera_aparicion():
    assert buscar_elemento([1, 2, 3, 2], 2) == 1
    print("Caso 4: Retornó la primera aparición del número")


if __name__ == "__main__":
    tests = [
        test_encuentra_numero,
        test_numero_no_encontrado,
        test_posicion_correcta,
        test_primera_aparicion,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError:
            print(f"FAILED: {test.__name__})")
            failed += 1

    print("-----------------------")
    print(f"Passed: {passed} | Failed: {failed}")
