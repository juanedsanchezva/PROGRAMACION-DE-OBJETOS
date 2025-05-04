#Algoritmo de Euclides para encontrar el GCD

a = int(input("Ingresa el primer numero: "))
b = int(input("Ingresa el segundo numero: "))

#Aplicar el algoritmo de Euclides
while b != 0:
    a, b = b, a % b

print(f"El maximo comun divisor (GCD) es: {a}")
