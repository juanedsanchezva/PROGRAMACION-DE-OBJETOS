#EJERCICIO LEY DE COULUMB 
#Bienvenido al código de coulumbinator, una calculadora de la fuerza entre dos cargas que utiliza la ley de coulumb

def coulumbinator():

    print ("Bienvenido a la calculadora de la ley de Coulumb\nencontrarás el valor de la fuerza entre dos cargas eléctricas") #Bienvenida al programa
    print ("_________________________________________________________________________________") #Este es un objeto de estética que funciona con el objetivo de separar secciones

    Q1 = float(input("Escribe el valor de la primera carga")) #Se define la variable Q1 que representa el valor de la carga 1
    Q2 = float(input("Escribe el valor de la segunda carga ")) #Se define la variable Q2 que representa el valor de la carga 2
    R = float (input("Escribe el valor de la distancia que hay entre estás cargas ")) #Se define la variable R que representa el valor de la distancia entre las cargas

    
    print ("_________________________________________________________________________________") #Este es un objeto de estética que funciona con el objetivo de separar secciones

    print(f"el resultado de la operación es {} enhorabuena") #Aquí se mostrará el resultado final

    return (coulumbinator()) #Retorna al usuario la función incial

coulumbinator()