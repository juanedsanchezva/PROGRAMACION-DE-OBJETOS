#Calculadora simple del area de un rectangulo if

#Solicitar datos al usuario
alto = float(input("Ingresa la altura del rectangulo (en metros): "))
ancho = float(input("Ingresa la anchura del rectangulo (en metros): "))

#Validar que los datos sean positivos
if alto > 0 and ancho > 0:
    area = alto * ancho    
    print(f"El area del rectangulo es: {area:.2f} metros cuadrados.")
else:
    print("Error: La altura y la anchura deben ser numeros positivos.")