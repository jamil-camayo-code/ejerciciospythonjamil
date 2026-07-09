# Datos:
codigo=1234
tarjeta_billetera = input("¿tarjeta o billetera?: ")
fondos = input("¿Tiene fondos suficientes? (si/no): ")
codigo_usuario = int(input("Ingrese codigo de seguridad: "))



# Verificacion: 

if (((tarjeta_billetera == "tarjeta" or tarjeta_billetera=="billetera") and fondos == "si" and codigo_usuario == codigo)):
    print("Pago aprobado.")
else:
    print("Pago rechazado.")