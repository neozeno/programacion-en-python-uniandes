def es_materia_favorita(nombre: str) -> bool:
    """
    Determina si una materia es del agrado de Pedro.

    Una materia le gusta a Pedro si su nombre contiene alguna
    de las palabras clave: "programacion", "matematica",
    "filosofia" o "literatura".

    Parámetros:
        nombre (str): Nombre de la materia en minúsculas y sin acentos.

    Retorna:
        bool: True si la materia es del agrado de Pedro, False en caso contrario.

    Ejemplos:
        >>> es_materia_favorita("introduccion a la programacion")
        True
        >>> es_materia_favorita("historia del arte")
        False
    """
    palabras_clave = ["programacion", "matematica", "filosofia", "literatura"]
    return any(palabra in nombre for palabra in palabras_clave)


def conteo_de_materias(materia_1: str, materia_2: str, materia_3: str) -> int:
    """
    Cuenta cuántas de las tres materias son del agrado de Pedro.

    Pedro disfruta las materias cuyos nombres contienen alguna
    de las siguientes palabras: "programacion", "matematica",
    "filosofia" o "literatura".

    Parámetros:
        materia_1 (str): Nombre de la primera materia.
        materia_2 (str): Nombre de la segunda materia.
        materia_3 (str): Nombre de la tercera materia.

    Retorna:
        int: Cantidad de materias (entre 0 y 3) que le gustan a Pedro.

    Ejemplos:
        >>> conteo_de_materias("calculo diferencial", "programacion web", "filosofia antigua")
        2
        >>> conteo_de_materias("historia", "quimica", "biologia")
        0
        >>> conteo_de_materias("matematica discreta", "literatura universal", "programacion orientada a objetos")
        3
    """
    materias = [materia_1, materia_2, materia_3]
    return sum(es_materia_favorita(m) for m in materias)
