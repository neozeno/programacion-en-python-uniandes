from typing import TypedDict


class Cancion(TypedDict):
    posicion: int
    nombre_cancion: str
    nombre_artista: str
    anio: int
    letra: str


class CancionNoLetra(TypedDict):
    posicion: int
    nombre_cancion: str
    nombre_artista: str
    anio: int


type ListaCanciones = list[Cancion]


def cargar_canciones(ruta: str) -> ListaCanciones:
    """
    Carga un archivo CSV de Billboard y retorna una lista de objetos Cancion.

    Parámetros:
        ruta (str): Ruta al archivo CSV.

    Retorna:
        ListaCanciones: Lista de canciones cargadas desde el archivo.

    Arroja:
        FileNotFoundError: Si el archivo no existe en la ruta indicada.
        ValueError: Si una línea del archivo tiene un formato inesperado.
        IOError: Si ocurre un problema leyendo el archivo.
    """
    canciones: ListaCanciones = []

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

            if len(lineas) == 0:
                raise ValueError(f"El archivo '{ruta}' está vacío.")

            for numero, linea in enumerate(lineas[1:], start=2):
                # Se divide solo en las primeras 4 cuatro comas para no alterar
                # la letra de la cancion
                info = linea.strip().split(",", 4)

                if len(info) < 5:
                    raise ValueError(
                        f"Línea {numero} tiene formato inválido: '{linea.strip()}'"
                    )

                try:
                    cancion: Cancion = {
                        "posicion": int(info[0]),
                        "nombre_cancion": info[1],
                        "nombre_artista": info[2],
                        "anio": int(info[3]),
                        "letra": info[4],
                    }
                except ValueError:
                    raise ValueError(
                        f"Línea {numero}: 'posicion' o 'anio' no son enteros válidos: '{linea.strip()}'"
                    )

                canciones.append(cancion)

    except FileNotFoundError:
        raise FileNotFoundError(f"No se encontró el archivo '{ruta}'.")
    except IOError as e:
        raise IOError(f"Error leyendo el archivo '{ruta}': {e}")

    return canciones


def buscar_canciones(
    canciones: ListaCanciones, nombre_cancion: str, anio: int
) -> Cancion | None:
    """
    Busca una canción en la lista por nombre y año del ranking.

    Parámetros:
        canciones (ListaCanciones): Lista completa de canciones.
        nombre_cancion (str): Nombre de la canción a buscar.
        anio (int): Año del ranking al que pertenece la canción.

    Retorna:
        Cancion | None: Diccionario con la información de la canción si se encuentra,
                        None si no existe en la lista.

    Ejemplos:
        >>> buscar_cancion(canciones, "wooly bully", 1965)
        {'posicion': 1, 'nombre_cancion': 'wooly bully', ...}
        >>> buscar_cancion(canciones, "cancion inexistente", 1965)
        None
    """
    for cancion in canciones:
        if cancion["nombre_cancion"] == nombre_cancion and cancion["anio"] == anio:
            return cancion

    return None


def encontrar_canciones_por_anio(
    canciones: ListaCanciones, anio: int
) -> list[CancionNoLetra]:
    canciones_por_anio: list[CancionNoLetra] = []

    for cancion in canciones:
        if cancion["anio"] == anio:
            canciones_por_anio.append(
                {
                    "posicion": cancion["posicion"],
                    "nombre_cancion": cancion["nombre_cancion"],
                    "nombre_artista": cancion["nombre_artista"],
                    "anio": cancion["anio"],
                }
            )

    return canciones_por_anio


def encontrar_canciones_por_artista_por_periodo(
    canciones: ListaCanciones, artista: str, anio_inicial: int, anio_final: int
) -> list[CancionNoLetra]:
    resultado: list[CancionNoLetra] = []

    for cancion in canciones:
        if cancion["nombre_artista"] == artista:
            if cancion["anio"] >= anio_inicial and cancion["anio"] <= anio_final:
                resultado.append(
                    {
                        "posicion": cancion["posicion"],
                        "nombre_cancion": cancion["nombre_cancion"],
                        "nombre_artista": cancion["nombre_artista"],
                        "anio": cancion["anio"],
                    }
                )

    return resultado


def encontrar_canciones_por_artista(
    canciones: ListaCanciones, artista: str
) -> list[CancionNoLetra]:
    canciones_por_artista: list[CancionNoLetra] = []

    for cancion in canciones:
        if cancion["nombre_artista"] == artista:
            canciones_por_artista.append(
                {
                    "posicion": cancion["posicion"],
                    "nombre_cancion": cancion["nombre_cancion"],
                    "nombre_artista": cancion["nombre_artista"],
                    "anio": cancion["anio"],
                }
            )

    return canciones_por_artista


def encontrar_artistas_por_cancion(
    canciones: ListaCanciones, nombre_cancion: str
) -> set[str]:
    resultado: set[str] = set()

    for cancion in canciones:
        if cancion["nombre_cancion"] == nombre_cancion:
            resultado.add(cancion["nombre_artista"])

    return resultado


def encontrar_artistas_con_minimo_canciones(
    canciones: ListaCanciones, numero_canciones: int
) -> dict[str, int]:
    """
    Encuentra los artistas que han tenido más canciones que el mínimo indicado
    a lo largo de todos los años en el Billboard.

    Cada aparición de una canción en un año distinto cuenta como una entrada
    independiente.

    Parámetros:
        canciones (ListaCanciones): Lista completa de canciones del Billboard.
        minimo (int): Cantidad mínima de canciones (exclusiva) que debe tener
                      un artista para aparecer en el resultado.

    Retorna:
        dict[str, int]: Diccionario con los nombres de los artistas que superan
                        el mínimo como llaves y su cantidad de canciones como valores.
                        Retorna un diccionario vacío si ningún artista cumple la condición.

    Ejemplos:
        >>> artistas_con_minimo_canciones([
        ...     {"nombre_artista": "the beatles", ...},
        ...     {"nombre_artista": "the beatles", ...},
        ...     {"nombre_artista": "elvis presley", ...},
        ... ], 1)
        {'the beatles': 2}
    """
    conteo: dict[str, int] = {}

    for cancion in canciones:
        artista = cancion["nombre_artista"]
        """
        .get(llave, valor_por_defecto) intenta obtener el valor asociado
        a artista en el diccionario. Si el artista no existe aún, en lugar
        de lanzar un KeyError retorna 0 (el valor por defecto). Si el artista
        ya existe, retorna su conteo actual.
        """
        conteo[artista] = conteo.get(artista, 0) + 1

    return {
        artista: total for artista, total in conteo.items() if total > numero_canciones
    }


def encontrar_artista_con_mas_canciones(canciones: ListaCanciones) -> dict[str, int]:
    """
    Encuentra el artista con mayor número de canciones en el Billboard
    a lo largo de todos los años.

    Cada aparición de una canción en un año distinto cuenta como una entrada
    independiente.

    Parámetros:
        canciones (list[Cancion]): Lista completa de canciones del Billboard.

    Retorna:
        dict[str, int]: Diccionario con el nombre del artista como llave
                        y su cantidad de canciones como valor.

    Ejemplos:
        >>> artista_mas_canciones([
        ...     {"nombre_artista": "the beatles", "anio": 1965, ...},
        ...     {"nombre_artista": "the beatles", "anio": 1966, ...},
        ...     {"nombre_artista": "elvis presley", "anio": 1965, ...},
        ... ])
        {'the beatles': 2}
    """
    conteo: dict[str, int] = {}

    for cancion in canciones:
        artista = cancion["nombre_artista"]
        conteo[artista] = conteo.get(artista, 0) + 1

    mejor_artista = max(conteo, key=lambda a: conteo[a])

    return {mejor_artista: conteo[mejor_artista]}


def encontrar_canciones_unicas_por_artista(
    canciones: ListaCanciones,
) -> dict[str, list[str]]:
    """
    Agrupa las canciones únicas de cada artista en un diccionario.

    Si una canción aparece más de una vez en el Billboard (en distintos años),
    se incluye una sola vez en la lista del artista.

    Parámetros:
        canciones (ListaCanciones): Lista completa de canciones del Billboard.

    Retorna:
        dict[str, list[str]]: Diccionario cuyas llaves son los nombres de los
                              artistas y los valores son listas con los nombres
                              únicos de sus canciones.

    Ejemplos:
        >>> canciones_por_artista([
        ...     {"nombre_artista": "the beatles", "nombre_cancion": "hey jude", "anio": 1965, ...},
        ...     {"nombre_artista": "the beatles", "nombre_cancion": "hey jude", "anio": 1966, ...},
        ...     {"nombre_artista": "the beatles", "nombre_cancion": "let it be", "anio": 1966, ...},
        ... ])
        {'the beatles': ['hey jude', 'let it be']}
    """
    resultado: dict[str, list[str]] = {}

    for cancion in canciones:
        artista = cancion["nombre_artista"]
        nombre = cancion["nombre_cancion"]

        if artista not in resultado:
            resultado[artista] = []

        if nombre not in resultado[artista]:
            resultado[artista].append(nombre)

    return resultado


def calcular_promedio_canciones_por_artista(canciones: ListaCanciones) -> float:
    """
    Calcula el promedio de canciones únicas por artista en el Billboard.

    La fórmula es:
        promedio = cantidad total de canciones diferentes / cantidad de artistas diferentes

    Tanto las canciones como los artistas se cuentan una sola vez,
    independientemente de cuántas veces aparezcan en el listado.

    Parámetros:
        canciones (ListaCanciones): Lista completa de canciones del Billboard.

    Retorna:
        float: Promedio de canciones únicas por artista, redondeado a dos decimales.

    Ejemplos:
        >>> promedio_canciones_por_artista([
        ...     {"nombre_artista": "the beatles", "nombre_cancion": "hey jude",  ...},
        ...     {"nombre_artista": "the beatles", "nombre_cancion": "hey jude",  ...},
        ...     {"nombre_artista": "the beatles", "nombre_cancion": "let it be", ...},
        ...     {"nombre_artista": "elvis presley", "nombre_cancion": "hound dog", ...},
        ... ])
        1.5
    """
    catalogo: dict[str, set[str]] = {}

    for cancion in canciones:
        artista = cancion["nombre_artista"]
        nombre = cancion["nombre_cancion"]

        if artista not in catalogo:
            catalogo[artista] = set()

        catalogo[artista].add(nombre)

    total_canciones: int = sum(
        len(canciones_artista) for canciones_artista in catalogo.values()
    )
    total_artistas: int = len(catalogo)

    return round(total_canciones / total_artistas, 2)
