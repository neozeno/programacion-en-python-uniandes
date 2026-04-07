def producto_mas_costoso(carrito: dict[str, int]) -> str | None:
    if len(carrito) == 0:
        return "No hay productos en el carrito"

    precio_mayor: int = max(carrito.values())

    candidatos: list[str] = [
        producto for producto, precio in carrito.items() if precio == precio_mayor
    ]

    return min(candidatos, key=lambda nombre: nombre.lower())


def test_carrito_vacio():
    assert producto_mas_costoso({}) == "No hay productos en el carrito"
    print("Caso 1: Carrito vacío retorna mensaje correcto")


def test_producto_mas_costoso():
    carrito: dict[str, int] = {"Flores": 5_000, "Chocolate": 8_000, "Peluche": 3_000}
    assert producto_mas_costoso(carrito) == "Chocolate"
    print("Caso 2: Retorna el producto más costoso")


def test_empate_alfabetico():
    catalogo: dict[str, int] = {"Bananos": 3_000, "Naranjas": 3_000}
    assert producto_mas_costoso(catalogo) == "Bananos"
    print("Caso 3: Empate resuelto alfabéticamente")


if __name__ == "__main__":
    tests = [
        test_carrito_vacio,
        test_producto_mas_costoso,
        test_empate_alfabetico,
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
