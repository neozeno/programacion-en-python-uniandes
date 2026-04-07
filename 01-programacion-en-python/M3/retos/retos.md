# Module 3: Retos

## Reto 8: Ash y la Liga Kalos

Ash Ketchum, el personaje principal del anime Pokémon, está a punto de luchar
en la final de la liga Kalos. En estos eventos compiten los mejores entrenadores
del mundo en batallas donde cada entrenador puede tener 3, 4, 5 o 6 criaturas.
Ash quiere saber, para una cantidad de criaturas específica, si él podrá formar
un equipo únicamente con Pokémon seudolegendarios para competir en la final.
Un pokemon seudolegendario es aquel que en la suma de sus estadísticas
de combate tiene 600 puntos o más.

Las estadísticas de combate de cada pokemon son 6:  

- ataque
- defensa
- ataque_especial
- defensa_especial
- velocidad
- vida

Escriba una función que, dada una lista de diccionarios (cada uno representando
un pokémon) con las anteriores estadísticas, determine si Ash podrá formar
un equipo de pokémon seudolegendarios para afrontar la final de la liga.
En caso que Ash pueda formar un equipo, retorne una lista con los nombres de
las criaturas que Ash utilizaría en la batalla. Si es imposible generar
un equipo que cumpla con las condiciones, retorne `None`.

Se garantiza que en caso de poder formar un equipo válido, solamente habrá
una configuración posible.  

La lista de retorno debe componerse únicamente de cadenas de caracteres
y debe tener el mismo orden de la lista que llega por parámetro.  

Su solución debe tener una función de acuerdo con la siguiente especificación:

- Nombre de la función: `construir_equipo_pokemon`

Si lo requiere, puede agregar funciones adicionales. 

### Descripción de parámetros

- `cantidad` (`int`): La cantidad de pokémones que usará cada entrenador
  en la batalla final. Es un entero entre 3 y 6.
- `equipo` (`list`): Una lista compuesta de diccionarios. Los diccionarios
  representan cada uno de los pokémon elegibles por Ash. Cada diccionario tiene
  las siguientes llaves: `"nombre": str` el nombre del pokemon, se garantiza
  que no hay nombres repetidos en los diccionarios de la lista; `"vida": int`,
  `"ataque": int`, `"defensa": int`, `"ataque_especial": int`,
  `"defensa_especial": int`, `"velocidad": int`. Cada uno de estos valores
  enteros representa la estadística de combate respectiva del pokémon.

### Descripción de retorno

- Tipo: `list`
- Descripción: `None` si es imposible generar un equipo de pokémones
  seudolegendarios para la batalla. De lo contrario, retorna una lista
  con los nombres de los pokémon a utilizar en la batalla.

### Solucion

```py
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
```
