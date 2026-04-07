from typing import TypeAlias, TypedDict


class Vuelo(TypedDict):
    aerolinea: str
    origen: str
    destino: str
    distancia: float
    retraso: int
    duracion: int
    salida: int


Itinerario: TypeAlias = dict[str, Vuelo]


def calcular_retraso_promedio(vuelos: Itinerario, aerolinea: str) -> float:
    """
    Calcula el retraso promedio de una aerolínea específica.

    Parámetros:
        vuelos (Itinerario): Diccionario de vuelos.
        aerolinea (str): Nombre de la aerolínea.

    Retorna:
        float: Retraso promedio en minutos.
    """
    vuelos_aerolinea = [
        vuelo["retraso"] for vuelo in vuelos.values() if vuelo["aerolinea"] == aerolinea
    ]

    return sum(vuelos_aerolinea) / len(vuelos_aerolinea)


def mejor_aerolinea(vuelos: Itinerario) -> str:
    """
    Determina la aerolínea con menor retraso promedio.

    Parámetros:
        vuelos (Itinerario): Diccionario de diccionarios con la información de los vuelos.

    Retorna:
        str: Nombre de la aerolínea con menor retraso promedio.

    Ejemplos:
        >>> mejor_aerolinea({
        ...     "AA100": {"aerolinea": "American", "retraso": 10, ...},
        ...     "DL200": {"aerolinea": "Delta",    "retraso": 5,  ...}
        ... })
        'Delta'
    """
    aerolineas: set[str] = {vuelo["aerolinea"] for vuelo in vuelos.values()}

    return min(aerolineas, key=lambda a: calcular_retraso_promedio(vuelos, a))


def test_mejor_aerolinea_simple():
    vuelos: Itinerario = {
        "AA100": {
            "aerolinea": "American",
            "origen": "JFK",
            "destino": "LAX",
            "distancia": 2475,
            "retraso": 20,
            "duracion": 360,
            "salida": 800,
        },
        "DL200": {
            "aerolinea": "Delta",
            "origen": "ATL",
            "destino": "ORD",
            "distancia": 606,
            "retraso": 5,
            "duracion": 120,
            "salida": 1200,
        },
    }
    assert mejor_aerolinea(vuelos) == "Delta"
    print("Caso 1: Identifica la aerolínea con menor retraso")


def test_multiples_vuelos_por_aerolinea():
    vuelos: Itinerario = {
        "AA100": {
            "aerolinea": "American",
            "origen": "JFK",
            "destino": "LAX",
            "distancia": 2475,
            "retraso": 10,
            "duracion": 360,
            "salida": 800,
        },
        "AA101": {
            "aerolinea": "American",
            "origen": "LAX",
            "destino": "JFK",
            "distancia": 2475,
            "retraso": 30,
            "duracion": 360,
            "salida": 1400,
        },
        "DL200": {
            "aerolinea": "Delta",
            "origen": "ATL",
            "destino": "ORD",
            "distancia": 606,
            "retraso": 15,
            "duracion": 120,
            "salida": 1200,
        },
        "DL201": {
            "aerolinea": "Delta",
            "origen": "ORD",
            "destino": "ATL",
            "distancia": 606,
            "retraso": 25,
            "duracion": 120,
            "salida": 1600,
        },
    }
    assert mejor_aerolinea(vuelos) == "Delta"
    print("Caso 2: Promedia correctamente múltiples vuelos por aerolínea")


def test_sin_retraso():
    vuelos: Itinerario = {
        "SW100": {
            "aerolinea": "Southwest",
            "origen": "DAL",
            "destino": "HOU",
            "distancia": 239,
            "retraso": 0,
            "duracion": 60,
            "salida": 700,
        },
        "UA200": {
            "aerolinea": "United",
            "origen": "SFO",
            "destino": "DEN",
            "distancia": 967,
            "retraso": 15,
            "duracion": 180,
            "salida": 900,
        },
    }
    assert mejor_aerolinea(vuelos) == "Southwest"
    print("Caso 3: Aerolínea sin retraso gana correctamente")


if __name__ == "__main__":
    tests = [
        test_mejor_aerolinea_simple,
        test_multiples_vuelos_por_aerolinea,
        test_sin_retraso,
    ]
    passed = 0
    failed = 0
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError:
            print(f"FAILED: {test.__name__}")
            failed += 1
    print("-----------------------")
    print(f"Passed: {passed} | Failed: {failed}")
