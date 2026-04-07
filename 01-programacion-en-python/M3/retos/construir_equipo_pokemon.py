from typing import TypeAlias, TypedDict


class Pokemon(TypedDict):
    nombre: str
    vida: int
    ataque: int
    ataque_especial: int
    defensa: int
    defensa_especial: int
    velocidad: int


Equipo: TypeAlias = list[Pokemon]


def es_seudolegendario(pokemon: Pokemon) -> bool:
    """
    Determina si un pokémon es seudolegendario.

    Un pokémon es seudolegendario si la suma de sus estadísticas
    de combate es mayor o igual a 600.

    Parámetros:
        pokemon (Pokemon): Diccionario con las estadísticas del pokémon.

    Retorna:
        bool: True si el pokémon es seudolegendario, False en caso contrario.

    Ejemplos:
        >>> es_seudolegendario({"nombre": "Dragonite", "vida": 91, "ataque": 134, "defensa": 95, "ataque_especial": 100, "defensa_especial": 100, "velocidad": 80})
        True
    """
    UMBRAL_SEUDOLEGENDARIO: int = 600
    total: int = (
        pokemon["vida"]
        + pokemon["ataque"]
        + pokemon["ataque_especial"]
        + pokemon["defensa"]
        + pokemon["defensa_especial"]
        + pokemon["velocidad"]
    )

    return total >= UMBRAL_SEUDOLEGENDARIO


def construir_equipo_pokemon(cantidad: int, equipo: Equipo) -> list[str] | None:
    """
    Construye un equipo de pokémon seudolegendarios para la liga Kalos.

    Filtra los pokémon seudolegendarios de la lista y verifica si hay
    suficientes para formar un equipo del tamaño requerido.

    Parámetros:
        cantidad (int): Número de pokémon necesarios para el equipo (entre 3 y 6).
        equipo(Equipo): Lista de diccionarios con los pokémon elegibles.

    Retorna:
        list[str]: Nombres de los pokémon del equipo en el mismo orden de la lista
                   original, o None si no es posible formar un equipo válido.

    Ejemplos:
        >>> construir_equipo_pokemon(2, [
        ...     {"nombre": "Dragonite", "vida": 91, "ataque": 134, "defensa": 95, "ataque_especial": 100, "defensa_especial": 100, "velocidad": 80},
        ...     {"nombre": "Pikachu",   "vida": 35, "ataque": 55,  "defensa": 40, "ataque_especial": 50,  "defensa_especial": 50,  "velocidad": 90}
        ... ])
        None
    """
    if cantidad < 3 or cantidad > 6:
        raise ValueError(
            f"La cantidad de pokemons a usar debe ser entre 3 y 6. Se recibio: {cantidad}"
        )

    seudolegendarios: list[str] = [
        pokemon["nombre"] for pokemon in equipo if es_seudolegendario(pokemon)
    ]

    if len(seudolegendarios) == cantidad:
        return seudolegendarios

    return None


dragonite: Pokemon = {
    "nombre": "Dragonite",
    "vida": 91,
    "ataque": 134,
    "defensa": 95,
    "ataque_especial": 100,
    "defensa_especial": 100,
    "velocidad": 80,
}
pikachu: Pokemon = {
    "nombre": "Pikachu",
    "vida": 35,
    "ataque": 55,
    "defensa": 40,
    "ataque_especial": 50,
    "defensa_especial": 50,
    "velocidad": 90,
}
rattata: Pokemon = {
    "nombre": "Rattata",
    "vida": 30,
    "ataque": 56,
    "defensa": 35,
    "ataque_especial": 25,
    "defensa_especial": 35,
    "velocidad": 72,
}
salamence: Pokemon = {
    "nombre": "Salamence",
    "vida": 95,
    "ataque": 135,
    "defensa": 80,
    "ataque_especial": 110,
    "defensa_especial": 80,
    "velocidad": 100,
}
tyranitar: Pokemon = {
    "nombre": "Tyranitar",
    "vida": 100,
    "ataque": 134,
    "defensa": 110,
    "ataque_especial": 95,
    "defensa_especial": 100,
    "velocidad": 61,
}


def test_equipo_valido():
    squad: Equipo = [dragonite, tyranitar, salamence, pikachu]
    resultado = construir_equipo_pokemon(3, squad)
    assert resultado == ["Dragonite", "Tyranitar", "Salamence"]
    print("Caso 1: Equipo válido construido correctamente")


def test_sin_suficientes_seudolegendarios():
    squad: Equipo = [dragonite, pikachu, rattata]
    resultado = construir_equipo_pokemon(3, squad)
    assert resultado is None
    print("Caso 2: Retorna None cuando no hay suficientes seudolegendarios")


def test_lista_vacia():
    squad: Equipo = []
    resultado = construir_equipo_pokemon(3, squad)
    assert resultado is None
    print("Caso 3: Retorna None con lista vacía")


if __name__ == "__main__":
    tests = [
        test_equipo_valido,
        test_sin_suficientes_seudolegendarios,
        test_lista_vacia,
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
