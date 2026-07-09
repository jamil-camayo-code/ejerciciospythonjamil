# Datos

verificada = input("¿La cuenta está verificada? (si/no): ")
normas = input("¿Acepta las normas de la plataforma? (si/no): ")
prohibidas = input("¿El contenido contiene palabras prohibidas? (si/no): ")

moderador = input("¿Es moderador? (si/no): ")
suspension = input("¿Tiene suspensión activa? (si/no): ")

# Verificacion 

if ((verificada == "si" and normas == "si" and prohibidas == "no") or moderador == "si") and suspension == "no":
    print("Puede publicar contenido.")
else:
    print("No puede publicar contenido.")