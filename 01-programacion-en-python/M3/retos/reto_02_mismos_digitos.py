def mismos_digitos(a: int, b: int) -> bool:
    """
    Determina si dos números enteros contienen exactamente los mismos dígitos,
    sin tener en cuenta el orden ni la frecuencia de aparición.

    Parámetros:
        a (int): Primer número entero positivo.
        b (int): Segundo número entero positivo.

    Retorna:
        bool: True si ambos números comparten los mismos dígitos, False en caso contrario.

    Ejemplos:
        >>> mismos_digitos(998, 89)
        True
        >>> mismos_digitos(123, 321)
        True
        >>> mismos_digitos(123, 456)
        False
    """
    return set(str(a)) == set(str(b))
