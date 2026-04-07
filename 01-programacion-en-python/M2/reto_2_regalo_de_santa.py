def es_palindromo(n: int) -> bool:
    """
    Determina si un número entero es palíndromo.

    Parámetros:
        n (int): El número a evaluar.

    Retorna:
        bool: True si el número es palíndromo, False en caso contrario.

    Ejemplos:
        >>> es_palindromo(121)
        True
        >>> es_palindromo(123)
        False
    """
    cadena = str(n)
    return cadena == cadena[::-1]


def clasificar_regalo(id: int) -> str:
    """
    Clasifica un regalo según su identificador numérico.

    Un identificador entre 100 y 999 determina el tipo de destinatario
    según las siguientes reglas:
        - Palíndromo e impar  → niña   ("girl")
        - Palíndromo y par    → niño   ("boy")
        - Par y no palíndromo → hombre ("man")
        - Impar y no palíndromo → mujer ("woman")

    Parámetros:
        id (int): Identificador único del regalo (entre 100 y 999).

    Retorna:
        str: "girl", "boy", "man" o "woman" según corresponda.

    Ejemplos:
        >>> clasificar_regalo(121)
        'girl'
        >>> clasificar_regalo(252)
        'boy'
        >>> clasificar_regalo(124)
        'man'
        >>> clasificar_regalo(123)
        'woman'
    """
    palindromo = es_palindromo(id)
    par = id % 2 == 0

    if palindromo and not par:
        return "girl"
    if palindromo and par:
        return "boy"
    if par and not palindromo:
        return "man"
    return "woman"
