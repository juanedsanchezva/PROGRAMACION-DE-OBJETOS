#Mostrar todos los numeros impares menores que el numero dado

numero = int(input("Ingresa un numero:"))


impares = []


 
for i in range(1, numero):
    if i % 2 != 0:  #Si el residuo de dividir entre 2 es distinto a 0 es impar
     
     impares.append(i) 

print(f"Numeros impares menores que {numero}:")
print(impares)