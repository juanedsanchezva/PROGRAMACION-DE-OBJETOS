import math


def potenciaCuadrada(x,y):
    z = x**y
    print(f"El resultado de la funcion es {z}")
    return z




def AreaDelCirculo(r):
    result = math.pi * potenciaCuadrada(r,2)
    #result = math.pi * r**2
    print(f"El area del circulo es {result}")

AreaDelCirculo(10)





def area_rectangulo(l, a):
   area = l * a
   return area  

largo = float(input("largo del rectangulo: "))
ancho = float(input("ancho del rectangulo: "))
print("El area del rectangulo es:", end = " ")
print(area_rectangulo(largo, ancho))