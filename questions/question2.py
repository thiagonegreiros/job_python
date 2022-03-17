# Escreva um procedimento que peça dois números do usuário e imprima seu produto
from unittest import result


def multiplication_between_two_numbers(number1, number2):
    return number1 * number2


n1 = int(input("Informe o primeiro numero: "))
n2 = int(input("Informe o segundo numero: "))
result = multiplication_between_two_numbers(2, 2)

print(f"O produto entre {n1} e {n2} é {result}")
