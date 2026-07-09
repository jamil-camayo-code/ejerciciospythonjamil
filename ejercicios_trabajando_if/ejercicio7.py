# Datos ingressados por pantalla
disponibilidad = input("¿La sala está disponible? (si/no): ")
asistentes = int(input("Ingrese el número de asistentes: "))
capacidad = int(input("Ingrese la capacidad de la sala: "))
anticipacion = int(input("¿Con cuántas horas de anticipación realiza la reserva?: "))

directivo = input("¿Es directivo? (si/no): ")
pendientes = input("¿Tiene reservas pendientes sin cancelar? (si/no): ")

# Verificcion
if ((disponibilidad == "si" and asistentes <= capacidad and anticipacion >= 24) or (directivo == "si" and disponibilidad == "si")) and pendientes == "no":
    print("Puede reservar la sala.")
else:
    print("No puede reservar la sala.")