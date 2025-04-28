import math #Lo invocamos para poder utilizar más adelante el numero "pi" ya que se utiliza en la fórmula de volumen

def Volumen(r1, h, r2): #Función que define variables como el radio 1, la altura y el radio 2 (r1, h y r2 respectivamente)

    print ("Vamos a calcular el volumen de un solido:")
    print ("________________________________________") #Este es un objeto de estética que funciona con el objetivo de separar secciones

# Volumen de la esfera
    volumen_esfera = (4/3) * math.pi * (r1 ** 3)
    print(f"El volumen de la esfera es: {volumen_esfera:.2f}m/3")

    # Volumen del cono
    volumen_cono = (1/3) * math.pi * (r2 ** 2) * h
    print(f"El volumen del cono es: {volumen_cono:.2f}m/3")

    # Volumen total
    volumen_total = volumen_esfera + volumen_cono

    print (f"El resultado final es {volumen_total:.2f}m/3 ¡Qué interesante!")
    print ("_________________________________________") #Este es un objeto de estética que funciona con el objetivo de separar secciones

Volumen(3, 9/2, 4) #Función, definiendo los valores a utilizar en r1, h y r2