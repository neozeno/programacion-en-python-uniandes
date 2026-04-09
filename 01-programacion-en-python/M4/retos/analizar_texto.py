def analizar_texto(
    texto: str, caracteres_permitidos: list[str]
) -> dict[str, tuple[int, int, int]]:
    """
    Analiza un texto y construye un diccionario con información sobre cada palabra.

    Una palabra es una secuencia contigua de caracteres permitidos. Cualquier
    carácter fuera de la lista se trata como separador.

    Parámetros:
        texto (str): Cadena de caracteres a analizar.
        caracteres_permitidos (list[str]): Caracteres que pueden formar palabras.

    Retorna:
        dict[str, tuple[int, int, int]]: Diccionario donde:
            - La llave es la palabra en minúscula.
            - La tupla contiene (cantidad, primera_posicion, ultima_posicion).

    Ejemplos:
        >>> analizar_texto("El gato y el perro", list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        {'el': (2, 0, 10), 'gato': (1, 3, 3), 'y': (1, 8, 8), 'perro': (1, 12, 12)}
    """
    permitidos: set[str] = set(caracteres_permitidos)
    resultado: dict[str, tuple[int, int, int]] = {}

    palabra_actual: str = ""
    inicio_actual: int = 0

    for i, caracter in enumerate(texto):
        if caracter.lower() in permitidos or caracter in permitidos:
            if not palabra_actual:
                inicio_actual = i
            palabra_actual += caracter
        else:
            if palabra_actual:
                _registrar_palabra(resultado, palabra_actual.lower(), inicio_actual)
                palabra_actual = ""

    if palabra_actual:
        _registrar_palabra(resultado, palabra_actual.lower(), inicio_actual)

    return resultado


def _registrar_palabra(
    resultado: dict[str, tuple[int, int, int]], palabra: str, posicion: int
) -> None:
    """
    Registra o actualiza una palabra en el diccionario de resultados.

    Parámetros:
        resultado (dict): Diccionario acumulador de palabras.
        palabra (str): Palabra en minúscula a registrar.
        posicion (int): Posición de inicio de la palabra en el texto original.
    """
    if palabra in resultado:
        cantidad, primera, _ = resultado[palabra]
        resultado[palabra] = (cantidad + 1, primera, posicion)
    else:
        resultado[palabra] = (1, posicion, posicion)


def test_palabra_repetida():
    permitidos = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    resultado = analizar_texto("El gato y el perro", permitidos)
    assert resultado["el"] == (2, 0, 10)
    assert resultado["gato"] == (1, 3, 3)
    print("Caso 1: Palabra repetida contada y posicionada correctamente")


def test_no_cuenta_subcadenas():
    permitidos = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    resultado = analizar_texto("el hielo", permitidos)
    assert resultado["el"] == (1, 0, 0)
    assert "el" in resultado
    assert resultado["hielo"] == (1, 3, 3)
    print("Caso 2: Subcadena dentro de palabra no contada como palabra independiente")


def test_caracteres_no_permitidos_como_separadores():
    permitidos = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    resultado = analizar_texto("hola,mundo.aqui", permitidos)
    assert "hola" in resultado
    assert "mundo" in resultado
    assert "aqui" in resultado
    print("Caso 3: Comas y puntos tratados como separadores")


def test_mayusculas_minusculas():
    permitidos = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    resultado = analizar_texto("Hola hola HOLA", permitidos)
    assert resultado["hola"] == (3, 0, 10)
    print("Caso 4: Mayúsculas y minúsculas tratadas como la misma palabra")


def test_garcia_marquez():
    permitidos = list(
        "abcdefghijklmnopqrstuvwxyzáéíóúüñABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚÜÑ"
    )
    texto = "Muchos años después, frente al pelotón de fusilamiento, el coronel Aureliano Buendía había de recordar aquella tarde remota en que su padre lo llevó a conocer el hielo."
    resultado = analizar_texto(texto, permitidos)
    assert resultado["el"][0] == 2
    assert resultado["el"][1] == 56
    assert resultado["el"][2] == 159
    assert resultado["de"][0] == 2
    assert resultado["de"][1] == 39
    assert resultado["de"][2] == 91
    print("Caso 5: Texto García Márquez analizado correctamente")


if __name__ == "__main__":
    tests = [
        test_palabra_repetida,
        test_no_cuenta_subcadenas,
        test_caracteres_no_permitidos_como_separadores,
        test_mayusculas_minusculas,
        test_garcia_marquez,
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
