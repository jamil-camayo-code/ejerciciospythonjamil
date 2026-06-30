#operaciones
num1 = int(input("Digite número 1: "))
num2 = int(input("Digite número 2: "))

op = input("Digite +, -, * o /: ")

resultado = 0

if op == "+":
    resultado = num1 + num2
    print("El resultado de la suma es:", resultado)

if op == "-":
    resultado = num1 - num2
    print("El resultado de la resta es:", resultado)

if op == "*":
    resultado = num1 * num2
    print("El resultado de la multiplicación es:", resultado)

if op == "/":
    if num2 != 0:
        resultado = num1 / num2
        print("El resultado de la división es:", resultado)
    else:
        print("Error: no se puede dividir entre cero.")

else:
    print("Operación no válida.")