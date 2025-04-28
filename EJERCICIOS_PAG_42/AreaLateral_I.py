import math #Se utiliza para poder invocar mas tarde el numero pi que hará parte de las fórmulas para solucionar el problema

def AreaVagon():
    
    print ("---- Datos ----")
    Radio = float(input("¿Cuál es el radio de las ruedas? ")) #Al ser un problema donde las ruedas del vagón son iguales entre si, significa que este radio es universal para todas (en este problema)
    Base = float (input("¿Cuál es el la base del vagón? ")) #Se pregunta al usuario a través de la consola la base del vagón
    Altura = float (input("¿Cuál es el la altura del vagón? ")) #Se pregunta al usuario a través de la consola la altura del vagón

   
    AreaRueda = math.pi * (Radio ** 2) # Area del vagon (circulo)

    
    AreaVagonRectangulo = Base * Altura  # Area del vagon (rectangulo)

    
    AreaTotal = AreaVagonRectangulo + (2 * AreaRueda) # Suma de areas (area del rectangulo + areas de las dos ruedas)

    print ("---- Resultados ----")
    print (f"El área del vagón terminó siendo {AreaTotal:.2f} m/2")
    print ("---- Fin del programa ----")

    return (AreaVagon()) #Retorna al usuario la función incial

AreaVagon()

