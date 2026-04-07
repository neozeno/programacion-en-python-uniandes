def picas_y_fijas(numero_secreto: int, intento: int) -> dict[str, int]:
    """
    Calcula el número de picas y fijas de un intento en el juego de Picas y Fijas.

    Una FIJA es un dígito que coincide en valor y posición con el número secreto.
    Una PICA es un dígito que existe en el número secreto pero está en posición incorrecta.

    Parámetros:
        numero_secreto (int): Número de 4 cifras con dígitos únicos que se debe adivinar.
        intento (int): Número de 4 cifras con el que el jugador intenta adivinar.

    Retorna:
        dict[str, int]: Diccionario con las llaves "PICAS" y "FIJAS" y sus respectivos conteos.

    Ejemplos:
        >>> picas_y_fijas(1234, 1325)
        {'PICAS': 2, 'FIJAS': 1}
        >>> picas_y_fijas(1234, 1234)
        {'PICAS': 0, 'FIJAS': 4}
        >>> picas_y_fijas(1234, 5678)
        {'PICAS': 0, 'FIJAS': 0}
    """
    numero_secreto_str = str(numero_secreto)
    intento_str = str(intento)

    """
    zip(secreto, intento) empareja los dígitos por posición:
        ('1','1'), ('2','3'), ('3','2'), ('4','5').
    Luego s == i evalúa cada par produciendo True/False,
    y sum() cuenta los True (que valen 1).
    Solo suma los dígitos que coinciden en valor y posición.
    """
    fijas = sum(s == i for s, i in zip(numero_secreto_str, intento_str))

    """
    Recorre cada dígito d del intento y pregunta si existe en algún lugar
    del secreto (d in secreto). sum() cuenta cuántos dígitos del intento
    aparecen en el secreto sin importar la posición.
    """
    picas = sum(d in numero_secreto_str for d in intento) - fijas

    return {"PICAS": picas, "FIJAS": fijas}
