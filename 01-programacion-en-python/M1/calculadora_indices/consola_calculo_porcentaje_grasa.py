from calculadora_indices import calcular_porcentaje_grasa


def consola_calculo_porcentaje_grasa():
    peso = float(input("Ingrese el peso de la persona (en kilogramos): "))
    altura = float(input("Ingrese la altura de la persona (en metros): "))
    edad = int(input("Ingrese la edad de la persona (en anos): "))
    valor_genero = float(
        input(
            "Ingrese el valor del genero de la persona (masculino: 10.8, femenino: 0): "
        )
    )
    porcentaje_grasa = round(
        calcular_porcentaje_grasa(peso, altura, edad, valor_genero), 2
    )

    print(f"{porcentaje_grasa}%")


consola_calculo_porcentaje_grasa()
