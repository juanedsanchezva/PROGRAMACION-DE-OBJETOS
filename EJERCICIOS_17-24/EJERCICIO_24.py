import math  # Para usar sqrt (raiz cuadrada)

#Leer coeficientes
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

#Verificar que no sea una ecuacion lineal
if a == 0:
    print("Esto no es una ecuación de segundo grado ya que a no puede ser 0.")
else:
#Calcular discriminante
    discriminante = b**2 - 4*a*c
    
#Estudiar las soluciones según el valor del discriminante
    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        print(f"Dos soluciones reales distintas: x1 = {x1}, x2 = {x2}")
    elif discriminante == 0:
        x = -b / (2*a)
        print(f"Una solución real doble: x = {x}")
    else:
        print("No tiene soluciones reales (discriminante negativo).")
