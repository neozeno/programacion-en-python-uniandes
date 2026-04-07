def aplicar_giro(orientacion: str, giro: str) -> str:
    """
    Aplica un único comando de giro a la orientación actual del robot.

    Parámetros:
        orientacion (str): Orientación actual ("N", "S", "E", "W").
        giro (str): Comando a aplicar ("L", "R", "H", ".").

    Retorna:
        str: Nueva orientación tras aplicar el comando.

    Ejemplos:
        >>> aplicar_giro("N", "R")
        'E'
        >>> aplicar_giro("N", "L")
        'W'
        >>> aplicar_giro("N", "H")
        'S'
        >>> aplicar_giro("N", ".")
        'N'
    """
    giro_derecha = {"N": "E", "E": "S", "S": "W", "W": "N"}
    giro_izquierda = {"N": "W", "W": "S", "S": "E", "E": "N"}
    media_vuelta = {"N": "S", "S": "N", "E": "W", "W": "E"}

    if giro == "R":
        return giro_derecha[orientacion]
    if giro == "L":
        return giro_izquierda[orientacion]
    if giro == "H":
        return media_vuelta[orientacion]
    return orientacion


def movimiento_robot(
    orientacion_actual: str, giro_1: str, giro_2: str, giro_3: str
) -> str:
    """
    Calcula la orientación final del robot tras aplicar tres comandos consecutivos.

    El robot parte de una orientación inicial y ejecuta tres giros en secuencia.
    Cada giro se aplica sobre el resultado del anterior.

    Parámetros:
        orientacion_actual (str): Orientación inicial del robot ("N", "S", "E", "W").
        giro_1 (str): Primer comando  ("L", "R", "H", ".").
        giro_2 (str): Segundo comando ("L", "R", "H", ".").
        giro_3 (str): Tercer comando  ("L", "R", "H", ".").

    Retorna:
        str: Orientación final del robot ("N", "S", "E", "W").

    Ejemplos:
        >>> movimiento_robot("N", "R", "R", "R")
        'W'
        >>> movimiento_robot("N", "H", ".", "L")
        'E'
        >>> movimiento_robot("E", "L", "H", "R")
        'E'
    """
    orientacion = aplicar_giro(orientacion_actual, giro_1)
    orientacion = aplicar_giro(orientacion, giro_2)
    orientacion = aplicar_giro(orientacion, giro_3)
    return orientacion
