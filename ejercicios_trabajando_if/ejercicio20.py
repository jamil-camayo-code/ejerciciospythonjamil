# Datos

entrega = input("¿Entregó el proyecto a tiempo? (si/no): ")
calificacion = float(input("Ingrese la calificación del proyecto: "))
documentacion = input("¿Incluye documentación técnica? (si/no): ")
pruebas = input("¿Supera las pruebas funcionales? (si/no): ")

plagio = input("¿Se detectó plagio? (si/no): ")
presentado = input("¿El proyecto fue presentado? (si/no): ")

# Verificacion

if ((entrega == "si" and calificacion >= 3.5 and documentacion == "si" and pruebas == "si") or (calificacion >= 4.5)) and plagio == "no" and presentado == "si":
    print("Proyecto aprobado.")
else:
    print("Proyecto no aprobado.")

