# Conversor de Euros a Dólares con validación usando if

# Tasa de conversión 
tasa_cambio = 1.13

# Pedir al usuario la cantidad en euros
euros = float(input("Ingresa la cantidad en euros: "))

# Validar que el monto sea positivo
if euros > 0:
    dolares = euros * tasa_cambio
    print(f"{euros:.2f} euros equivalen a {dolares:.2f} dólares.")
else:
    print("Por favor, ingresa una cantidad positiva de euros.")
