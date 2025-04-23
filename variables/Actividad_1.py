#string

print("hola ya se imprimir frases")



#float

float = 452
print(float)

float = 44.5
print(float)

 
#suma
x = 15 + 32
print(x)

#resta
x = 1232 - 532
print(x)

#mutiplicacion
x = 1232 * 532
print(x)

#division
x = 1232 / 532
print(x)

#Imprime los numeros del 1 al 3
for x in range(1, 4):
    print(x)

#Imprime los numeros del 1 al 9
for x in range(1, 10):
    print(x)

#Imprime los numeros del 1 al 10.000
for x in range(1, 10000):
    print(x)

#Alternativa imprimir los numeros del 1 al 10.000
x = 1
a = []
while(x<=10000):
    a.append(x)
    x+=1
print(a)

#Imprime los numeros del 5 al 10
for x in range(5, 11):
    print(x)

#Imprime los numeros del 5 al 15
for x in range(5, 16):
    print(x)



#Imprime los numeros del 5 al 15.000
for x in range(5, 15000):
    print(x)

#Alternativa imprimir los numeros del 5 al 15.000
x = 5
a = []
while(x<=15000):
    a.append(x)
    x+=5
print(a)

#imprimir hola 200 veces
palabra = "hola"

for _ in range(200):
    print(palabra)

#Alternativa hola 200 veces
palabra = "hola"
a = []
for _ in range(200):
    a.append(palabra)
print(a)

#Imprimir los cuadrados de los 30 primeros numeros naturales
for x in range(1, 31):
    print(f"El cuadrado de {x} es {x**2}")


#Imprimir multiplique los 20 primeros número naturales 
resultado = 1
for x in range(1, 21):
    resultado *= x  
print(f"El producto de los 20 primeros numeros naturales es: {resultado}")

#Imprimir suma cuadrados de los primeros 100 numeros naturales
suma_cuadrados = 0
for i in range(1, 101):
    suma_cuadrados += i**2 
print(f"La suma de los cuadrados de los 100 primeros números naturales es: {suma_cuadrados}")

