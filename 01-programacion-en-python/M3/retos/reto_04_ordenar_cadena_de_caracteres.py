def ordenar_cadena(cadena: str) -> str:
    """
    Ordena alfabéticamente los caracteres de una cadena.

    Parámetros:
        cadena (str): Cadena compuesta únicamente de letras minúsculas del alfabeto inglés.

    Retorna:
        str: La cadena con sus caracteres ordenados alfabéticamente.

    Ejemplos:
        >>> ordenar_cadena("bca")
        'abc'
        >>> ordenar_cadena("zyxw")
        'wxyz'
        >>> ordenar_cadena("a")
        'a'
    """
    return "".join(sorted(cadena))
