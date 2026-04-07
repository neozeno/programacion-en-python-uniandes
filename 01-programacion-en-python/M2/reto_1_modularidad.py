def es_divisible(n: int, d: int) -> int:
    """
    Determina si n es divisible por 2d, por d, o por ninguno.

    Parámetros:
        n (int): El número que se quiere evaluar.
        d (int): El divisor base. Si es 0, retorna 0 directamente.

    Retorna:
        int: 2 si n es divisible por 2d,
             1 si n es divisible por d pero no por 2d,
             0 en cualquier otro caso.

    Ejemplos:
        >>> es_divisible(12, 3)
        2
        >>> es_divisible(9, 3)
        1
        >>> es_divisible(7, 3)
        0
        >>> es_divisible(5, 0)
        0
    """
    if d == 0:
        return 0
    if n % (2 * d) == 0:
        return 2
    if n % d == 0:
        return 1
    return 0
