#CLASIFICACION DE EDADES

edad = int(input("escribe tu edad  "))

if edad < 13 and edad >= 0:
    print("eres un niño")

elif edad >= 13 and edad <= 17:
    print("eres un adolecente")

elif edad >= 18 and edad <= 59:
    print("eres un adulto")

elif edad >= 60:
    print("eres un adulto mayor")

elif edad < 0:
    print("el numero de tu edad debe ser positivo")