#Esta es una función que calcula las vueltas (o lo que se queda debiendo) de una encomienda común

def Vueltas(P , M , H): #Cada una de las variables significa Panes, Bolsas de leche y Huevos respectivamente
    
    Pprecio = P * 300 #Cada uno de los numeros por los que se multiplica es el precio individual de cada producto                                       
    Mprecio = M * 3300 
    Hprecio = H * 350  

    # Sumatoria del costo total
    Total = Pprecio + Mprecio + Hprecio
    print("---- TOTAL ----")
    print(f"El total de la compra es: {Total} pesos.")
    Paga = int(input("¿Con cuanto dinero pagarás? "))
    print("---- VUELTAS ----")
    Vueltas = Paga - Total

    if (Vueltas >= 0):
        print(f" Tus vueltas son: {Vueltas} pesos.")
    else:
        print(f" Quedas debiendo {-Vueltas} pesos.")  # Se pone negativo en positivo
 

# Testeo pidiendo datos al usuario
print ("---- DATOS ----")
P = int(input("¿Cuántos panes deseas? "))
M = int(input("¿Cuántas bolsas de leche deseas? "))
H = int(input("¿Cuántos huevos deseas? "))

Vueltas(P, M, H)