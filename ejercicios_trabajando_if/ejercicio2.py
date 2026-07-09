# Datos ingresados por el usuario

compra = float(input("Ingrese el valor de la compra: "))

ciudad = input("¿La entrega es dentro de la ciudad? (si/no): ")
premium = input("¿El cliente es premium? (si/no): ")
envio_especial = input("¿El producto tiene envío especial? (si/no): ")


# Verificar si aplica el envío gratuito
if ((compra >= 150000 and ciudad == "si") or (premium == "si" and compra > 80000)) and envio_especial == "no":
    print("Aplica envío gratuito.")
else:
    print("No aplica envío gratuito.")