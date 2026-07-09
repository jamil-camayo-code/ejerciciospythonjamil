# Datos

modulos = input("¿Aprobó todos los módulos requeridos? (si/no): ")
promedio = float(input("Ingrese el promedio del aprendiz: "))
hoja_vida = input("¿Entregó hoja de vida? (si/no): ")

empresa = input("¿Una empresa lo solicita directamente? (si/no): ")
disciplinario = input("¿Tiene proceso disciplinario abierto? (si/no): ")

# Verificacion: 

if ((modulos == "si" and promedio >= 3.8 and hoja_vida == "si") or empresa == "si") and disciplinario == "no":
    print("Puede ser seleccionado.")
else:
    print("No puede ser seleccionado.")
    