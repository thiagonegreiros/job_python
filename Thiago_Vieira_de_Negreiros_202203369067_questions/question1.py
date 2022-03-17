# Escreva uma função que receba cinco números inteiros e devolva o maior deles
def verify_max_number(number1, number2, number3, number4, number5):
    return max(number1, number2, number3, number4, number5)


n1 = int(input("Informe o primeiro numero: "))
n2 = int(input("Informe o segundo numero: "))
n3 = int(input("Informe o terceiro numero: "))
n4 = int(input("Informe o quarto numero: "))
n5 = int(input("Informe o quinto numero: "))
larger = verify_max_number(n1, n2, n3, n4, n5)
print(f"O maior número é: { larger }")
