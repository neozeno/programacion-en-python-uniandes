def producto_mas_barato(catalogo: dict[str, int]) -> str | None:
    if len(catalogo) == 0:
        return "No hay productos para escoger"

    precio_menor: int = min(catalogo.values())

    if precio_menor > 10_000:
        return None

    candidatos: list[str] = [
        producto for producto, precio in catalogo.items() if precio == precio_menor
    ]

    return min(candidatos, key=lambda nombre: nombre.lower())


def test_catalogo_vacio():
    assert producto_mas_barato({}) == "No hay productos para escoger"
    print("Caso 1: Catálogo vacío retorna mensaje correcto")


def test_producto_mas_barato():
    catalogo: dict[str, int] = {"Flores": 5_000, "Chocolate": 8_000, "Peluche": 3_000}
    assert producto_mas_barato(catalogo) == "Peluche"
    print("Caso 2: Retorna el producto más barato")


def test_empate_alfabetico():
    catalogo: dict[str, int] = {"Rosas": 3_000, "Anillo": 3_000}
    assert producto_mas_barato(catalogo) == "Anillo"
    print("Caso 3: Empate resuelto alfabéticamente")


def test_todos_caros():
    catalogo: dict[str, int] = {"Collar": 15_000, "Anillo": 20_000}
    assert producto_mas_barato(catalogo) is None
    print("Caso 4: Retorna None cuando todos los productos son mayores a 10.000")


if __name__ == "__main__":
    tests = [
        test_catalogo_vacio,
        test_producto_mas_barato,
        test_empate_alfabetico,
        test_todos_caros,
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
