# solicite si es estudiante tiene carnet=>descuento
estudiante=input("Es estudiante escriba: T o t si es estudiante o F o f si no lo es: ")
carnet=input("Escriba 0 si tiene carnet o 1 si no lo tiene: ")
#validacion:

if (estudiante=="T" or estudiante=="t") and carnet=="0":
    print("Descuento aprobado")
else:
    print("Descuento rechazado")