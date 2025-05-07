#Sume los cuadrados de los cien primeros numeros naturales

suma = 0  

for i in range(1, 101):
    suma += i ** 2

print(f"La suma de los cuadrados de los 100 primeros numeros naturales es {suma}")
