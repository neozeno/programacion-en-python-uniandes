from calculadora_indices import calcular_calorias_en_actividad


def consola_calculo_calorias_reposo():
    peso = float(input("Ingrese el peso de la persona (en kilogramos): "))
    altura = float(input("Ingrese la altura de la persona (en centimetros): "))
    edad = int(input("Ingrese la edad de la persona (en anos): "))
    valor_genero = int(
        input(
            "Ingrese el valor del genero de la persona (masculino: 5, femenino: -161): "
        )
    )
    calorias_reposo = round(
        calcular_calorias_en_actividad(peso, altura, edad, valor_genero), 2
    )

    print(f"{calorias_reposo} cal")


consola_calculo_calorias_reposo()
