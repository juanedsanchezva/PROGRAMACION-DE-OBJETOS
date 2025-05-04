#Comparar dos numeros y decir cual es mayor y cual es menor

#Pedir al usuario los dos numeros
Num1 = float(input("Ingresa el primer numero: "))
Num2 = float(input("Ingresa el segundo numero: "))

#Comparar los nUmeros 
if Num1 > Num2:
    print(f"El numero mayor es: {Num1}")
    print(f"El numero menor es: {Num2}")
elif Num2 > Num1:
    print(f"El numero mayor es: {Num2}")
    print(f"El numero menor es: {Num1}")
else:
    print("Ambos numeros son iguales.")
