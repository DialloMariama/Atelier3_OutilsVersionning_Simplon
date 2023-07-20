def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Division par zéro n'est pas autorisée."

num1 = 11
num2 = 25
result = division(num1, num2)
print("Résultat de la division :", result)
