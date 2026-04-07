from typing import TypeAlias

Estudiante: TypeAlias = dict[str, float | str]
Curso: TypeAlias = list[Estudiante]


def aproximar_nota(nota: float) -> float:
    """
    Aproxima una nota según las reglas de la Universidad de los Andes.

    Parámetros:
        nota (float): Nota sin aproximar.

    Retorna:
        float: Nota aproximada.

    Ejemplos:
        >>> aproximar_nota(4.7)
        5.0
        >>> aproximar_nota(3.8)
        4.0
        >>> aproximar_nota(2.9)
        3.0
        >>> aproximar_nota(2.0)
        1.5
    """
    if nota >= 4.5:
        return 5.0
    elif nota >= 3.5:
        return 4.0
    elif nota >= 2.5:
        return 3.0
    else:
        return 1.5


def calcular_definitivas(estudiantes: Curso) -> Curso:
    resultado: Curso = []

    for estudiante in estudiantes:
        resultado.append(
            {
                "nombre": estudiante["nombre"],
                "nota": aproximar_nota(float(estudiante["nota"])),
            }
        )

    return resultado


if __name__ == "__main__":
    notas = [
        {"nombre": "Anna", "nota": 4.6},
        {"nombre": "Bob", "nota": 3.9},
        {"nombre": "Charlie", "nota": 3.4},
        {"nombre": "Diane", "nota": 2.6},
        {"nombre": "Edward", "nota": 1.8},
    ]
    definitivas = calcular_definitivas(notas)
    print(definitivas)
