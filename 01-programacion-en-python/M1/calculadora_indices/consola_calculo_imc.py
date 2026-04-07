from calculadora_indices import calcular_IMC


def consola_calculo_imc():
    peso = float(input("Ingrese el peso de la persona (en kilogramos): "))
    altura = float(input("Ingrese la altura de la persona (en metros): "))
    imc = round(calcular_IMC(peso, altura), 2)

    print(imc)


consola_calculo_imc()
