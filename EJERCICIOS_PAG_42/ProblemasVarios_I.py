#Bienvenidos al calculador de carne

def CarneTotal(N , M , K): #Cada una de las variables significa gallinas, gallos y pollitos respectivamente
    
    NCarne = N * 6 #Cada uno de los numeros por los que se multiplica es el peso de la carne en kilogramos, en este caso cada gallina pesa 6 kilogramos
    MCarne = M * 7 # Cada gallo pesa 7 kg
    KCarne = K * 1  # Cada pollito pesa 1 kg 

 # Sumatoria total
    CarneTOTAL = NCarne + MCarne + KCarne
    

    print (f"El peso total de la carne es {CarneTOTAL:.2f} kilogramos") #Respuesta
# Testeamos pidiendo al usuario los valores
N = int(input("¿Cuántas gallinas tienes? "))
M = int(input("¿Cuántos gallos tienes? "))
K = int(input("¿Cuántos pollitos tienes? "))

CarneTotal(N, M, K)
 


