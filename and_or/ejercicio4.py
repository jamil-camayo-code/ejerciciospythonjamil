
nombre_usuario=input("Ingrese nombre de usuario: ")
contraseña=input("Ingrese Contraseña: ")

#Validacion

if (nombre_usuario=="admin" and contraseña=="sena2026") or (nombre_usuario=="invitado" and contraseña=="12345"):
    print("acceso permitido") 
else: 
    print("acceso denegado")