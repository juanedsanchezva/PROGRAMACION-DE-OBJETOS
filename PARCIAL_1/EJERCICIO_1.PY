#SUMA DE POSITIVOS Y PARES

numero1 = int(input("escriba un primer numero positivo par  "))
numero2 = int(input("escriba un segundo numero positivo par  "))
numero3 = int(input("escriba un tercer numero positivo par  "))
numero4 = int(input("escriba un cuarto numero positivo par  "))
numero5 = int(input("escriba un quinto numero positivo par  "))

if numero1 <= 0:
    print("el numero tiene que ser positivo")
    numero1 % 2 != 0
    print("el numero tiene que ser par")

else:
    numero1 > 0
    numero1 % 2 == 0

    print(f"el primer numero ({numero1}) es positivo y par")
      
    
if numero2 <= 0:
    print("el numero tiene que ser positivo")
    numero2 % 2 != 0
    print("el numero tiene que ser par")


else:
    numero2 > 0
    numero2 % 2 == 0

    print(f"el segundo numero ({numero2}) es positivo y par")


if numero3 <= 0:
    print("el numero tiene que ser positivo")
    numero3 % 2 != 0
    print("el numero tiene que ser par")

else:
    numero3 > 0
    numero3 % 2 == 0

    print(f"el tercer numero ({numero3}) es positivo y par")


if numero4 <= 0:
    print("el numero tiene que ser positivo")
    numero4 % 2 != 0
    print("el numero tiene que ser par")

else:
    numero4 > 0
    numero4 % 2 == 0

    print(f"el cuarto numero ({numero4}) es positivo y par")


if numero5 <= 0:
    print("el numero tiene que ser positivo")
    numero5 % 2 != 0
    print("el numero tiene que ser par")

else:
    numero5 > 0
    numero5 % 2 == 0

    print(f"el quinto numero ({numero5}) es positivo y par")

if numero1 <= 0 or numero2 <= 0 or numero3 <= 0 or numero4 <= 0 or numero5 <= 0:
    print("Hay uno o mas numeros negativos")
    numero1 % 2 != 0 or numero2 % 2 != 0 or numero3 % 2 != 0 or numero4 % 2 != 0 or numero5 % 2 != 0
    print("Hay uno o mas numeros impares")
    

else: suma = numero1 + numero2 + numero3 + numero4 + numero5
print(f"la suma de los 5 digitos es {suma}")




