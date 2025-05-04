# Programa para sumar los 100 números siguientes a uno dado

numero = int(input("Ingresa un número entero: "))

# Verificamos que sea un número positivo (ejemplo de uso de 'if')
if numero >= 0:
    suma = 0
    for i in range(numero + 1, numero + 101):
        suma += i
    print(f"La suma de los 100 números siguientes a {numero} es: {suma}")
else:
    print("Por favor, ingresa un número entero positivo.")
