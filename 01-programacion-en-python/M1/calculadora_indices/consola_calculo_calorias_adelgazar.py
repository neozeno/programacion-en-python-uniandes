from calculadora_indices import consumo_calorias_recomendado_para_adelgazar


def consola_calculo_calorias_adelgazar():
    peso = float(input("Ingrese el peso de la persona (en kilogramos): "))
    altura = float(input("Ingrese la altura de la persona (en centimetros): "))
    edad = int(input("Ingrese la edad de la persona (en anos): "))
    valor_genero = int(
        input(
            "Ingrese el valor del genero de la persona (masculino: 5, femenino: -161): "
        )
    )
    calorias_recomendadas = consumo_calorias_recomendado_para_adelgazar(
        peso, altura, edad, valor_genero
    )

    print(calorias_recomendadas)


consola_calculo_calorias_adelgazar()
