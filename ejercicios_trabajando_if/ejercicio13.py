# Datos
induccion = input("¿Aprobó la inducción de seguridad? (si/no): ")
proteccion = input("¿Usa los elementos de protección requeridos? (si/no): ")
reserva = input("¿Tiene reserva confirmada? (si/no): ")

instructor = input("¿Es instructor responsable del laboratorio? (si/no): ")
alerta = input("¿Hay una alerta de seguridad activa? (si/no): ")

# Verificion
if ((induccion == "si" and proteccion == "si" and reserva == "si") or instructor == "si") and alerta == "no":
    print("Puede ingresar al laboratorio.")
else:
    print("No puede ingresar al laboratorio.")