# Datos
credencial = input("¿Tiene credencial autorizada? (si/no): ")
biometria = input("¿Tiene biometría validada? (si/no): ")
horario = input("¿Está dentro del horario permitido? (si/no): ")

emergencia = input("¿Es personal de emergencia? (si/no): ")
evacuacion = input("¿Hay protocolo de evacuación activo? (si/no): ")

# Verificacion

if ((credencial == "si" and biometria == "si" and horario == "si") or emergencia == "si") and evacuacion == "no":
    print("Puede ingresar.")
else:
    print("No puede ingresar.")