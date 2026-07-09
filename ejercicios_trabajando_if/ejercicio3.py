
matriculado = input("¿Está matriculado? (si/no): ")
internet = input("¿Tiene conexión a internet? (si/no): ")
camara = input("¿La cámara funciona? (si/no): ")
autorizacion = input("¿Tiene autorización del instructor? (si/no): ")
aula = input("¿Está en un aula presencial? (si/no): ")
bloqueada = input("¿La cuenta está bloqueada? (si/no): ")

# Verificar si puede presentar el examen

if ((matriculado == "si" and internet == "si" and camara == "si") or (autorizacion == "si" and aula == "si")) and bloqueada == "no":
    print("Puede presentar el examen.")
else:
    print("No puede presentar el examen.")