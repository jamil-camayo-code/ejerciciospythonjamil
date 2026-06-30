#el usuario elige una puerta de tres, el jugador gana si acierta en la puerta ganadora

puerta_premiada=2
puerta_usuario=int(input("Elegir puerta del 1 al 3: "))

if puerta_premiada==puerta_usuario:
    print("Puerta premiada")
else:
    print("Puerta incorrecta")