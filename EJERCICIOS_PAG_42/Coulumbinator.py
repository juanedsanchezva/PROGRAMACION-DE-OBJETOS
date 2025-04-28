#EJERCICIO LEY DE COULUMB 
#Bienvenido al código de coulumbinator, una calculadora de la fuerza entre dos cargas que utiliza la ley de coulumb

def coulumbinator():

    print ("Bienvenido a la calculadora de la ley de Coulumb\nencontrarás el valor de la fuerza entre dos cargas eléctricas") #Bienvenida al programa
    print ("_________________________________________________________________________________") #Este es un objeto de estética que funciona con el objetivo de separar secciones

    Q1 = float(input("Escribe el valor de la primera carga(en Coulombs)")) #Se define la variable Q1 que representa el valor de la carga 1
    Q2 = float(input("Escribe el valor de la segunda carga(en Coulombs) ")) #Se define la variable Q2 que representa el valor de la carga 2
    r = float (input("Escribe el valor de la distancia que hay entre estás cargas(en metros) ")) #Se define la variable R que representa el valor de la distancia entre las cargas
    print("___________________________")

    # Constante de Coulomb (en N*m^2/C^2)
    k = 8.9875e9

    # Cálculo de la fuerza
    F = k * abs(Q1 * Q2) / (r ** 2)
    
    print ("_________________________________________________________________________________") #Este es un objeto de estética que funciona con el objetivo de separar secciones

    print(f"el resultado de la operación es {F:.2e} Newtons enhorabuena") #Aquí se mostrará el resultado final

    return (coulumbinator()) #Retorna al usuario la función incial

coulumbinator()