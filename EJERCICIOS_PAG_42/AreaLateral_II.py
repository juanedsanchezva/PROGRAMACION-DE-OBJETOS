import math #Se importa para poder invocar luego el número pi

def AreaCirculo(r): #Se define una función previamente que vamos a llamar Area de circulo
    pi = math.pi 
    AreaCIRCULO = float(pi*(r**2)) #Fórmula del Área de un circulo
    print (f"el resultado del área es {AreaCIRCULO:.2f} m/2 vamooooos")
    return AreaCIRCULO #Se escribe return para que al momento de usarlo en otra función nos dé el resultado, nos de el área 

def AreaRectangulo(b , h): #definimos dos variables que luego se pueden sustituir en la función "AreaCarro"
    AreaRECTANGULO = float(b*h) #Fórmula del Área de un rectángulo
    print (f"el área será {AreaRECTANGULO:.2f} m/2 vamoooooos")
    return AreaRECTANGULO

def AreaCarro():
    print("---- Datos de las ruedas ----")
    r1 = float(input("¿Cuál es el radio de la primera rueda? "))
    r2 = float(input("¿Cuál es el radio de la segunda rueda? "))
    
    print("---- Datos del vagon ----")
    b1 = float(input("¿Cuál es la base del vagon 1? "))
    h1 = float(input("¿Cuál es la altura del vagon 1? "))
    b2 = float(input("¿Cuál es la base del vagon 2? "))
    h2 = float(input("¿Cuál es la altura del vagon 2? "))
    print("---- Resultados ----")
    
   

    # Calculamos áreas usando las funciones
    print ("---- Area de la rueda 1 ----")
    area_rueda1 = AreaCirculo(r1)
    print ("---- Area de la rueda 2 ----")
    area_rueda2 = AreaCirculo(r2)
    print ("---- Area del vagon 1 (grande) ----")
    area_vagon1 = AreaRectangulo(b1, h1)
    print ("---- Area del vagon 2 (pequeño) ----")
    area_vagon2 = AreaRectangulo(b2, h2)
   
    Area_total = area_rueda1 + area_rueda2 + area_vagon1 + area_vagon2  # Sumatoria de áreas
   
    print (f"El area final del carro es {Area_total:.2f} m/2 WOOOOOOW")  
    print ("---- Fin del programa ----")
    
    return (AreaCarro()) #Retorna al usuario la función incial

AreaCarro()