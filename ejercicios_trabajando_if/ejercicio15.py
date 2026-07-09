# Datos
empresa = input("¿Pertenece a una empresa aliada? (si/no): ")
identificacion = input("¿Presenta identificación laboral? (si/no): ")
compra = float(input("Ingrese el valor de la compra: "))

codigo = input("¿Tiene un código promocional vigente? (si/no): ")
combina = input("¿Está combinando promociones no acumulables? (si/no): ")

# Verificacion 

if ((empresa == "si" and identificacion == "si" and compra > 100000) or codigo == "si") and combina == "no":
    print("Recibe descuento.")
else:
    print("No recibe descuento.")