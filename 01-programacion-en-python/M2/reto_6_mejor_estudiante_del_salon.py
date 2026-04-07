def calcular_promedio(estudiante: dict[str, float]) -> float:
    materias = ["matematicas", "español", "ciencias", "literatura", "arte"]
    total = 0

    for materia in materias:
        total += estudiante[materia]

    return total / 5


def mejor_del_salon(
    estudiante1: dict[str, float],
    estudiante2: dict[str, float],
    estudiante3: dict[str, float],
    estudiante4: dict[str, float],
    estudiante5: dict[str, float],
) -> str:
    estudiantes = [estudiante1, estudiante2, estudiante3, estudiante4, estudiante5]

    mejor_promedio = 0
    mejor_nombre = ""

    for estudiante in estudiantes:
        promedio = calcular_promedio(estudiante)
        nombre = str(estudiante["nombre"])

        if promedio > mejor_promedio:
            mejor_promedio = promedio
            mejor_nombre = nombre
        elif promedio == mejor_promedio:
            if nombre.lower() < mejor_nombre.lower():
                mejor_nombre = nombre

    return mejor_nombre
