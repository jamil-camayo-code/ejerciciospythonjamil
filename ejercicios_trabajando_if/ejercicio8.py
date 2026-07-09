# Datos

puntos = int(input("Ingrese los puntos obtenidos: "))
pruebas = int(input("Ingrese el número de pruebas en las que participó: "))

sanciones = input("¿Recibió sanciones? (si/no): ")
gano = input("¿Ganó una prueba principal? (si/no): ")
lesion = input("¿Presenta una lesión certificada que le impida competir? (si/no): ")

# Verificacion

if ((puntos >= 75 and pruebas >= 3 and sanciones == "no") or gano == "si") and lesion == "no":
    print("Clasifica.")
else:
    print("No clasifica.")