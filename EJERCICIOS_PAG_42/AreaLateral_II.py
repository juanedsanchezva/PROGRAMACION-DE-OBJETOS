import math #Se importa para poder invocar luego el número pi

def AreaCirculo(r): #Se define una función previamente que vamos a llamar Area de circulo
    pi = math.pi 
    AreaCIRCULO = float(pi*(r**2)) #Fórmula del Área de un circulo
    print (f"el resultado del área es {AreaCIRCULO} vamooooos")
    return AreaCIRCULO #Se escribe return para que al momento de usarlo en otra función nos dé el resultado, nos de el área 

def AreaRectángulo(b , h): #definimos dos variables que luego se pueden sustituir en la función "AreaCarro"
    AreaRECTANGULO = float(b*h) #Fórmula del Área de un rectángulo
    print (f"el área será {AreaRECTANGULO} vamoooooos")
    return AreaRECTANGULO

#LUEGO IMPLEMENTAR EN LA FUNCIÓN PRINCIPAL "AREA VAGON"

def AreaCarro():
    
    #IMPLEMENTAR LAS FORMULAS RESPECTIVAS TENIENDO EN CUENTA QUE UNA RUEDA ES DISTINTA DE OTRA, UTILIZANDO LAS FUNCIONES PREVIAMENTE DEFINIDAS
    #IMPLEMENTAR LAS FORMULAS RESPECTIVAS TENIENDO EN CUENTA QUE LAS CABINAS (RECTANGULOS) SON DIFERNTES ENTRE SI
    #IMPLEMENTAR SUMATORIA DE ÁREAS

    print (f"El area final del carro es {} WOOOOOOW")

AreaCarro()

    