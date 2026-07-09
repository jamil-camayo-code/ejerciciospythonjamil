# Datos
conexion = float(input("Ingrese el porcentaje de tiempo conectado a la sesión: "))

actividad = input("¿Participó en al menos una actividad? (si/no): ")
encuesta = input("¿Respondió la encuesta final? (si/no): ")

excusa = input("¿Tiene una excusa válida aprobada por el instructor? (si/no): ")
suplantacion = input("¿Se detectó suplantación? (si/no): ")

# Verificacion
if ((conexion >= 80 and actividad == "si" and encuesta == "si") or excusa == "si") and suplantacion == "no":
    print("El aprendiz queda presente.")
else:
    print("El aprendiz no queda presente.")