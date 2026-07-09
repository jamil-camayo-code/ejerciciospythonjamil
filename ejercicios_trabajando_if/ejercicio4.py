# datos por pantalla
promedio = float(input("Ingrese el promedio del estudiante: "))
asistencia = float(input("Ingrese el porcentaje de asistencia: "))
distancia = float(input("Ingrese la distancia a la institución (km): "))

evento = input("¿Representa a la institución en un evento nacional? (si/no): ")
faltas = input("¿Tiene faltas disciplinarias graves? (si/no): ")

# Verificar beca
if ((promedio >= 4.2 and asistencia > 90 and distancia > 5) or evento == "si") and faltas == "no":
    print("Recibe la beca.")
else:
    print("No recibe la beca.")