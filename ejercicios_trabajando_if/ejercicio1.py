nota = float(input("Ingrese la nota del curso: "))
asistencia = float(input("Ingrese el porcentaje de asistencia: "))
prueba_nivelacion = float(input("Ingrese el puntaje de la prueba de nivelación: "))

sancion = input("¿Tiene sanción académica activa? (si/no): ")



# Verificar si puede inscribirse
if ((nota >= 3.5 and asistencia > 80) or prueba_nivelacion >= 85) and sancion == "no":
    print("Puede inscribirse.")
else:
    print("No puede inscribirse.")