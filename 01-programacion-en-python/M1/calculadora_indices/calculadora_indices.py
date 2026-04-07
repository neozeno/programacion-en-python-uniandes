def calcular_IMC(peso: float, altura: float) -> float:
    """Calcula el indice de masa corporal de una persona

    Parametros
    ----------
    peso : float
        Peso de la persona en kilogramos
    altura : float
        Altura de la persona en metros

    Retorna
    -------
    float
        Índice de masa corporal de la persona
    """

    return peso / (altura**2)


def calcular_porcentaje_grasa(
    peso: float, altura: float, edad: int, valor_genero: float
) -> float:
    """Calcula el porcentaje de grasa de una persona

    Parametros
    ----------
    peso : float
        Peso de la persona en kilogramos
    altura : float
        Altura de la persona en metros
    edad : int
        Edad de la persona en años
    valor_genero : float
        Valor que varía según el género de la persona.
        masculino: 10.8, femenino: 0

    Retorna
    -------
    float
        El porcentaje de grasa que tiene el cuerpo de la persona
    """

    indice_masa_corporal = calcular_IMC(peso, altura)
    return (1.2 * indice_masa_corporal) + (0.23 * edad) - 5.4 - valor_genero


def calcular_calorias_en_reposo(
    peso: float, altura: float, edad: int, valor_genero: int
) -> float:
    """Calcula la cantidad de calorías que una persona quema estando en reposo
    (esto es, su tasa metabólica basal)

    Parametros
    ----------
    peso : float
        Peso de la persona en kilogramos
    altura : float
        Altura de la persona en metros
    edad : int
        Edad de la persona en años
    valor_genero : float
        Valor que varía según el género de la persona.
        masculino: 5, femenino: -161

    Retorna
    -------
    float
        La cantidad de calorías que la persona quema en reposo
    """

    return (10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero


def calcular_calorias_en_actividad(
    peso: float, altura: float, edad: int, valor_genero: int, valor_actividad: float
) -> float:
    """Calcula la cantidad de calorías que una persona quema al realizar algún
    tipo de actividad física (esto es, su tasa metabólica basal según actividad física)

    Parametros
    ----------
    peso : float
        Peso de la persona en kilogramos
    altura : float
        Altura de la persona en metros
    edad : int
        Edad de la persona en años
    valor_genero : float
        Valor que varía según el género de la persona.
        masculino: 5, femenino: -161
    valor_actividad : float
        Valor que depende de la actividad física semanal y toma
        uno de los siguiente valores: (1.2, 1.375, 1.55, 1.72, 1.9)

    Retorna
    -------
    float
        La cantidad de calorías que una persona quema, al realizar algún
        tipo de actividad física semanalmente
    """

    tasa_metabolica_basal = calcular_calorias_en_reposo(
        peso, altura, edad, valor_genero
    )
    valores_actividad = (1.2, 1.375, 1.55, 1.725, 1.9)

    if valor_actividad not in valores_actividad:
        raise ValueError("El valor de actividad provisto es invalido.")

    return tasa_metabolica_basal * valor_actividad


def consumo_calorias_recomendado_para_adelgazar(
    peso: float, altura: float, edad: int, valor_genero: int
) -> str:
    """
    Calcula el rango de calorías recomendado que debe consumir una persona,
    diariamente en caso de que desee adelgazar

    Parametros
    ----------
    peso : float
        Peso de la persona en kilogramos
    altura : float
        Altura de la persona en metros
    edad : int
        Edad de la persona en años
    valor_genero : int
        Valor que varía según el género de la persona:
        masculino = 5, femenino = -161

    Retorna
    -------
    str
        Una cadena indicando el rango de calorías que una persona
        debe consumir si desea adelgazar
    """
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    limite_inferior = round(tmb * 0.80, 2)
    limite_superior = round(tmb * 0.85, 2)
    recomendacion = f"Para adelgazar es recomendado que consumas entre: {limite_inferior} y {limite_superior} calorías al día."

    return recomendacion
