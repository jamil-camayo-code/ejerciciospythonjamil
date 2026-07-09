#el ejercicio se logro en parte con ayuda de chat gpt

usuario = input("Ingrese el usuario: ")
contrasena = input("Ingrese la contraseña: ")

verificacion = input("¿Tiene activada la verificación en dos pasos? (si/no): ")
cuenta = input("¿La cuenta está activa? (si/no): ")

acceso = input("¿Tiene un acceso temporal generado por un administrador? (si/no): ")
pais = input("¿Se conecta desde un país autorizado? (si/no): ")

# Datos correctos
usuario_correcto = "admin"
contrasena_correcta = "1234"

# Verificar si puede ingresar
if (((usuario == usuario_correcto and contrasena == contrasena_correcta) and verificacion == "si" and cuenta == "si") or acceso == "si") and pais == "si":
    print("Puede ingresar al sistema.")
else:
    print("No puede ingresar al sistema.")