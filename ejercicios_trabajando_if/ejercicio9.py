# Datos
valor = float(input("Ingrese el valor de la compra: "))

presupuesto = input("¿Tiene presupuesto disponible? (si/no): ")
supervisor = input("¿Tiene aprobación del supervisor? (si/no): ")
proveedor = input("¿El proveedor está registrado? (si/no): ")

# Verifiicacion

if ((valor <= 500000 and presupuesto == "si") or (valor > 500000 and presupuesto == "si" and supervisor == "si")) and proveedor == "si":
    print("Compra aprobada.")
else:
    print("Compra rechazada.")