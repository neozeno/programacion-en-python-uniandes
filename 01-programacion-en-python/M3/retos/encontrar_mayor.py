def encontrar_mayor(entrada: list[int]) -> int:
    """
    Itera sobre una lista de enteros positivos y retorna el numero mayor.

    Parámetros:
        entrada (list[int]): Lista en la que se buscará el número.

    Retorna:
        int: Numero mayor, o -1 si la lista esta vacia.

    Raise:
        ValueError: si la lista contiene algun numero negativo.

    Ejemplos:
        >>> buscar_elemento([1, 2, 3, 4])
        4
        >>> buscar_elemento([])
        -1
    """
    if len(entrada) == 0:
        return -1

    for numero in entrada:
        if numero < 0:
            raise ValueError(
                f"La lista solo debe contener numeros positivos. Se encontro {numero}"
            )

    numero_mayor = entrada[0]
    for numero in entrada:
        if numero > numero_mayor:
            numero_mayor = numero

    return numero_mayor


def test_lista_vacia():
    assert encontrar_mayor([]) == -1
    print("Caso 1: Lista vacia retorna -1")


def test_encuntra_numero_mayor():
    assert encontrar_mayor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    print("Caso 2: Encuentra el numero mayor correctamente")


def test_numero_negativo():
    try:
        assert encontrar_mayor([1, -2, 3])
        print("FAILED: debio lanzar ValueError")
    except ValueError:
        print("Caso 3: Se arrojo ValueError por numero negativo")


if __name__ == "__main__":
    tests = [
        test_lista_vacia,
        test_encuntra_numero_mayor,
        test_numero_negativo,
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
