
# Datos por pantalla

ingresos = float(input("Ingrese sus ingresos mensuales: "))
historial = input("¿Tiene historial crediticio positivo? (si/no): ")
deudas = input("¿Tiene deudas vencidas? (si/no): ")

codeudor = input("¿Tiene codeudor? (si/no): ")

if codeudor == "si":
    ingresos_codeudor = float(input("Ingrese los ingresos del codeudor: "))
else:
    ingresos_codeudor = 0

fraude = input("¿Aparece reportado por fraude? (si/no): ")


# Verificacion de crédito
if ((ingresos > 2000000 and historial == "si" and deudas == "no") or ingresos_codeudor > 3000000) and fraude == "no":
    print("Crédito aprobado.")
else:
    print("Crédito rechazado.")