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
    valor_actividad = float(
        input(
            "Ingrese el valor de la actividad (uno de los siguiente valores: (1.2, 1.375, 1.55, 1.72, 1.9))"
        )
    )
    calorias_actividad = round(
        calcular_calorias_en_actividad(
            peso, altura, edad, valor_genero, valor_actividad
        ),
        2,
    )

    print(f"{calorias_actividad} cal")


consola_calculo_calorias_reposo()
