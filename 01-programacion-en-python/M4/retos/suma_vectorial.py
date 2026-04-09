type Vector = tuple[float, float, float]


def suma_vectorial(vector_1: Vector, vector_2: Vector) -> Vector:
    v1_x, v1_y, v1_z = vector_1
    v2_x, v2_y, v2_z = vector_2

    return (v1_x + v2_x, v1_y + v2_y, v1_z + v2_z)


vector_vacio: Vector = (0, 0, 0)
vector_positivo: Vector = (1, 4, 3)
vector_negativo: Vector = (-4, -1, -3)
vector_mixto: Vector = (5, -7, 2)


def test_suma_vectores_vacios() -> None:
    assert suma_vectorial(vector_vacio, vector_vacio) == (0, 0, 0)
    print("Sumó correctamente dos vectores iguales a (0, 0, 0).")


def test_suma_vector_positivo_y_vacio() -> None:
    assert suma_vectorial(vector_vacio, vector_positivo) == (1, 4, 3)
    print("Sumó correctamente un vector vacio y uno con valores positivos")


def test_suma_vector_negativo_y_vacio() -> None:
    assert suma_vectorial(vector_vacio, vector_negativo) == (-4, -1, -3)
    print("Sumó correctamente un vector vacio y uno con valores negativos")


def test_suma_vectores_positivos() -> None:
    assert suma_vectorial(vector_positivo, vector_positivo) == (2, 8, 6)
    print("Sumó correctamente dos vectores con valores positivos")


def test_suma_vectores_negativos() -> None:
    assert suma_vectorial(vector_negativo, vector_negativo) == (-8, -2, -6)
    print("Sumó correctamente dos vectores con valores negativos")


def test_suma_vectores_positivo_y_mixto() -> None:
    assert suma_vectorial(vector_positivo, vector_mixto) == (6, -3, 5)
    print(
        "Sumó correctamente un vector con valores positivos y otro con valores mixtos"
    )


def test_suma_vectores_negativo_y_mixto() -> None:
    assert suma_vectorial(vector_negativo, vector_mixto) == (1, -8, -1)
    print(
        "Sumó correctamente un vector con valores negativos y otro con valores mixtos"
    )


if __name__ == "__main__":
    tests = [
        test_suma_vectores_vacios,
        test_suma_vector_positivo_y_vacio,
        test_suma_vector_negativo_y_vacio,
        test_suma_vectores_positivos,
        test_suma_vectores_negativos,
        test_suma_vectores_positivo_y_mixto,
        test_suma_vectores_negativo_y_mixto,
    ]
    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError:
            print(f"FAILED: {test.__name__}")
            failed += 1
    print("-----------------------")
    print(f"Passed: {passed} | Failed: {failed}")
