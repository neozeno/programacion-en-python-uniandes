def sucesion_fibonacci(cantidad_numeros: int) -> str:
    """
    Genera los primeros N números de la sucesión de Fibonacci.

    La sucesión comienza en 0 y 1, y cada número siguiente es la suma
    de los dos anteriores: 0, 1, 1, 2, 3, 5, 8, 13, ...

    Parámetros:
        cantidad_numeros (int): Cantidad de números de la sucesión a generar.

    Retorna:
        str: Números de la sucesión separados por coma y sin espacios.

    Ejemplos:
        >>> sucesion_fibonacci(6)
        '0,1,1,2,3,5'
        >>> sucesion_fibonacci(18)
        '0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597'
    """
    sucesion: list[int] = []
    a, b = 0, 1

    for _ in range(cantidad_numeros):
        sucesion.append(a)  # Agrega el número actual a la lista
        a, b = b, a + b  # Avanza: el nuevo 'a' es 'b', el nuevo 'b' es su suma

    return ",".join(str(n) for n in sucesion)
