#Calculadora de contagios

def calculadora_contagios():  #definimos funcion
    print("Bienvenido a la calculadora de contagios de Covid-19")
    print("_______________________________________________________")
    C = int(input("Escribe el número de contagiados actuales: "))
    D = int(input("Escribe el número de días a partir de hoy: "))

    print("_______________________________________________________")

    # Calculo del numero total de contagiados
    total_contagiados = C * (2 ** D)

    print(f"El numero total de personas contagiadas después de {D} dias sera: {total_contagiados}")
    print("_______________________________________________________")

    return (calculadora_contagios())

calculadora_contagios()