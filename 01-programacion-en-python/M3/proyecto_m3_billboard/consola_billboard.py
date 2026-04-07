"""
Poryecto M3: Billboard.
Interfaz basada en consola para la interacción con el usuario.

Temas:
* Instrucciones repetitivas.
* Listas
* Diccionarios
* Archivos
"""

import billboard as bb


def ejecutar_cargar_canciones() -> list[bb.Cancion]:
    """
    Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de
    las canciones y las carga.

    Retorno: list
        La lista de canciones con la información del archivo.
    """
    canciones: list[bb.Cancion] = []
    archivo = input("Por favor ingrese el nombre del archivo CSV con las canciones: ")

    try:
        canciones = bb.cargar_canciones(archivo)
        print("Se cargaron", len(canciones), "canciones a partir del archivo.")
    except FileNotFoundError as e:
        print(
            f"El archivo seleccionado no es válido. No se pudieron cargar las canciones del Ranking\n{e}"
        )
    except ValueError as e:
        print(f"Error de formato: {e}")
    except IOError as e:
        print(f"Error de lectura: {e}")

    return canciones


def ejecutar_buscar_cancion(canciones: list[bb.Cancion]) -> None:
    """
    Ejecuta la opción de buscar una canción dado el nombre y el año del
    ranking al cual pertenece
    """
    nombre_cancion = input(
        "Por favor ingrese el nombre de la canción que desea buscar: "
    )
    anio = int(input("Por favor ingrese el año de la canción que desea buscar: "))

    resultado: bb.Cancion | None = bb.buscar_canciones(canciones, nombre_cancion, anio)

    if resultado is None:
        print(f'La cancion "{nombre_cancion}" del anio {anio} no se encontro.')
    else:
        print(f"""Informacion de la cancion:
        - Nombre: {resultado["nombre_cancion"]}
        - Artista: {resultado["nombre_artista"]}
        - Anio: {resultado["anio"]}
        - Posicion: {resultado["posicion"]}
        - Letra: {resultado["letra"]}
        """)


def ejecutar_canciones_anio(canciones: list[bb.Cancion]) -> None:
    """Ejecuta la opción de consultar las canciones de un año dado"""
    anio = int(input("Por favor ingrese el año que desea consultar: "))

    canciones_por_anio: list[bb.CancionNoLetra] = bb.encontrar_canciones_por_anio(
        canciones, anio
    )

    print(canciones_por_anio)


def ejecutar_canciones_artista_periodo(
    canciones: list[bb.Cancion],
) -> None:
    """Ejecuta la opción de consultar las canciones de un artista dado en
    un periodo de tiempo definido
    """
    artista = input("Por favor ingrese el nombre del artista que desea buscar: ")
    anio_inic = int(input("Por favor ingrese el año inicial que desea buscar: "))
    anio_fin = int(input("Por favor ingrese el año final que desea buscar: "))

    resultado: list[bb.CancionNoLetra] = bb.encontrar_canciones_por_artista_por_periodo(
        canciones, artista, anio_inic, anio_fin
    )

    print(resultado)


def ejecutar_todas_canciones_artista(
    canciones: list[bb.Cancion],
) -> None:
    """Ejecuta la opción de consultar todas las canciones de un artista dado"""
    artista = input("Por favor ingrese el nombre del artista que desea buscar: ")

    resultado: list[bb.CancionNoLetra] = bb.encontrar_canciones_por_artista(
        canciones, artista
    )

    print(resultado)


def ejecutar_todos_artistas_cancion(canciones: list[bb.Cancion]) -> None:
    """Ejecuta la opción de consultar todos los artistas que han interpretado
    una canción dada
    """
    artista = input("Por favor ingrese el nombre de la canción que desea buscar: ")

    resultado: set[str] = bb.encontrar_artistas_por_cancion(canciones, artista)

    print(resultado)


def ejecutar_artistas_mas_populares(canciones: bb.ListaCanciones) -> None:
    """Ejecuta la opción de consultar los artistas más populares"""
    min = int(
        input("Por favor ingrese la cantidad mínima de canciones que desea buscar: ")
    )

    resultado: dict[str, int] = bb.encontrar_artistas_con_minimo_canciones(
        canciones, min
    )

    print(resultado)


def ejecutar_artista_estrella(canciones: bb.ListaCanciones) -> None:
    """Ejecuta la opción de consultar el artista estrella de todos los tiempos"""
    print(bb.encontrar_artista_con_mas_canciones(canciones))


def ejecutar_artistas_y_sus_canciones(canciones: bb.ListaCanciones) -> None:
    """Ejecuta la opción de consultar la lista completa de artistas del Billboard
    junto con sus canciones
    """
    print(bb.encontrar_canciones_unicas_por_artista(canciones))


def ejecutar_promedio_canciones_por_artista(canciones: bb.ListaCanciones) -> None:
    """Ejecuta la opción de consultar la cantidad promedio de canciones que los
    artistas tienen en el listado de Billboard
    """
    print(bb.calcular_promedio_canciones_por_artista(canciones))


def mostrar_menu():
    """Imprime las opciones de ejecución disponibles para el usuario."""
    print("\nOpciones")
    print("1. Cargar un archivo de canciones")
    print("2. Buscar una canción")
    print("3. Consultar las canciones de un año")
    print("4. Consultar las canciones de un artista en un periodo")
    print("5. Consultar todas las canciones de un artista")
    print("6. Consultar todos los artistas que han interpretado una canción")
    print("7. Consultar los artistas más populares")
    print("8. Consultar el artista estrella de todos los tiempos")
    print("9. Consultar los artistas y sus canciones")
    print("10. Consultar la cantidad promedio de canciones por artista")
    print("11. Salir.")


def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar = True
    canciones: list[bb.Cancion] = []

    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opción: "))
        if opcion_seleccionada == 1:
            canciones = ejecutar_cargar_canciones()
        elif opcion_seleccionada == 2:
            ejecutar_buscar_cancion(canciones)
        elif opcion_seleccionada == 3:
            ejecutar_canciones_anio(canciones)
        elif opcion_seleccionada == 4:
            ejecutar_canciones_artista_periodo(canciones)
        elif opcion_seleccionada == 5:
            ejecutar_todas_canciones_artista(canciones)
        elif opcion_seleccionada == 6:
            ejecutar_todos_artistas_cancion(canciones)
        elif opcion_seleccionada == 7:
            ejecutar_artistas_mas_populares(canciones)
        elif opcion_seleccionada == 8:
            ejecutar_artista_estrella(canciones)
        elif opcion_seleccionada == 9:
            ejecutar_artistas_y_sus_canciones(canciones)
        elif opcion_seleccionada == 10:
            ejecutar_promedio_canciones_por_artista(canciones)
        elif opcion_seleccionada == 11:
            continuar = False
        else:
            print("Por favor seleccione una opción válida.")


# PROGRAMA PRINCIPAL
iniciar_aplicacion()
