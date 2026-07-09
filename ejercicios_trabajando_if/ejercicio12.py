# Datos
permiso = input("¿Tiene permiso firmado? (si/no): ")
lista = input("¿Aparece en la lista oficial? (si/no): ")
seguro = input("¿Cuenta con seguro vigente? (si/no): ")

acudiente = input("¿El acudiente lo acompaña? (si/no): ")
restriccion = input("¿Tiene restricción médica activa? (si/no): ")

# Verificación

if ((permiso == "si" and lista == "si" and seguro == "si") or acudiente == "si") and restriccion == "no":
    print("Puede salir a la actividad.")
else:
    print("No puede salir a la actividad.")