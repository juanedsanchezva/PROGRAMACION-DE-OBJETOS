#Bienvenido al calculador de pago de préstamo

def prestamo(p, t): #definimos variables que significan préstamo y momento de pago (en meses)    
    print ("---- DATOS ----")
    print ("Este programa utiliza una tasa de interés del 3%")
    i = float(0.03) #Se define la tasa de interés del prestamos (3%) por ello lo denotamos en su escritura decimal 0.03
    PagoFinal= p * ((1 + i) ** t)  # Fórmula de interés compuesto
    print(f"El valor del pago es de: \n${PagoFinal} pesos") #Se pone \n para hacer un salto de linea, resultado del pago de prestamo


print("Bienvenido a Pagonaitor")
p = int(input("¿Valor prestamo? "))
t = int(input("¿momento de pago? (meses) "))

prestamo (p, t)