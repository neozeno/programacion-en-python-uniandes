def valor_carrito_compras(carrito: dict[str, float]) -> float:
    if len(carrito) == 0:
        return 0

    total: float = 0

    for precio in carrito.values():
        total += precio

    return total


def test_carrito_vacio():
    assert valor_carrito_compras({}) == float(0)
    print("Caso 1: Carrito vacío retorna total correcto")


def test_producto_mas_costoso():
    carrito: dict[str, float] = {"Flores": 5_000, "Chocolate": 8_000, "Peluche": 3_000}
    assert valor_carrito_compras(carrito) == float(16_000)
    print("Caso 2: Retorna el total correcto")


if __name__ == "__main__":
    tests = [
        test_carrito_vacio,
        test_producto_mas_costoso,
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
