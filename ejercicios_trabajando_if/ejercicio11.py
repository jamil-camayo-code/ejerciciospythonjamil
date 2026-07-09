# Datos
licencia = input("¿Tiene licencia vigente? (si/no): ")
revision = input("¿Aprobó la revisión de seguridad? (si/no): ")
combustible = input("¿El vehículo tiene combustible suficiente? (si/no): ")

emergencia = input("¿Es conductor de emergencia autorizado? (si/no): ")
comparendos = input("¿Tiene comparendos pendientes? (si/no): ")

# Verificacion

if ((licencia == "si" and revision == "si" and combustible == "si") or emergencia == "si") and comparendos == "no":
    print("Puede usar el vehículo.")
else:
    print("No puede usar el vehículo.")