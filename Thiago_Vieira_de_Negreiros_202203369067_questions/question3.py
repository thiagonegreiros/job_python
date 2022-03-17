# Escreva um programa que peça um número do usuário e imprima se o número
# informado é primo ou não
def prime_number(number):
    cont = 0
    for x in range(1, (number + 1)):
        if (number % x == 0):
            cont += 1

    if (cont == 2):
        return "primo"
    else:
        return "não primo"


number = int(input("Informe o número: "))
result = prime_number(number)

print(f"O número {number} é {result}")
