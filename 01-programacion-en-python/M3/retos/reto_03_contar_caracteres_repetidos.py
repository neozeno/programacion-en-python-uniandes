def contar_caracteres_repetidos(cadena: str) -> int:
    """
    Cuenta la cantidad de caracteres distintos que aparecen más de una vez en una cadena.

    Parámetros:
        cadena (str): Cadena compuesta únicamente de letras minúsculas del alfabeto inglés.

    Retorna:
        int: Número de caracteres diferentes que se repiten al menos una vez.

    Ejemplos:
        >>> contar_caracteres_repetidos("aabbcc")
        3
        >>> contar_caracteres_repetidos("abcd")
        0
        >>> contar_caracteres_repetidos("aabbc")
        2
    """
    frecuencia: dict[str, int] = {}

    for caracter in cadena:
        frecuencia[caracter] = frecuencia.get(caracter, 0) + 1

    return sum(1 for cantidad in frecuencia.values() if cantidad > 1)
