import math #Se importa para poder invocar luego el número pi

def AreaCirculo(r): #Se define una función previamente que vamos a llamar Area de circulo
    pi = math.pi 
    Area= float(pi*(r**2)) #Fórmula del Área de un circulo
    print (f"el resultado del área es {Area} vamooooos")
    return Area #Se escribe return para que al momento de usarlo en otra función nos dé el resultado, nos de el área 

def AreaRectángulo(b , h): #definimos dos variables que luego se pueden sustituir en la función "AreaCarro"

#IMPLEMENTAR AQUÍ LA FUNCIÓN DE AREA_RECTANGULO SIGUIENDO LA FORMULA DEL ÁREA DE UN RECTÁNGULO
#LUEGO IMPLEMENTAR EN LA FUNCIÓN PRINCIPAL "AREA VAGON"

def AreaCarro():
    
    #IMPLEMENTAR LAS FORMULAS RESPECTIVAS TENIENDO EN CUENTA QUE UNA RUEDA ES DISTINTA DE OTRA, UTILIZANDO LAS FUNCIONES PREVIAMENTE DEFINIDAS
    #IMPLEMENTAR LAS FORMULAS RESPECTIVAS TENIENDO EN CUENTA QUE LAS CABINAS (RECTANGULOS) SON DIFERNTES ENTRE SI
    #IMPLEMENTAR SUMATORIA DE ÁREAS

    print (f"El area final del carro es {} WOOOOOOW")

AreaCarro()

    