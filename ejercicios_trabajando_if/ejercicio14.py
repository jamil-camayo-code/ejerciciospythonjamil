# Datos
dias = int(input("Ingrese los días desde la compra: "))

factura = input("¿Tiene factura? (si/no): ")
danos = input("¿Presenta daños por mal uso? (si/no): ")
defectuoso = input("¿El producto llegó defectuoso? (si/no): ")
empaque = input("¿Tiene empaque original? (si/no): ")

personalizado = input("¿El artículo fue personalizado? (si/no): ")

# Verificacion

if ((dias <= 30 and factura == "si" and danos == "no") or defectuoso == "si") and personalizado == "no":
    print("Devolución aceptada.")
else:
    print("Devolución no aceptada.")