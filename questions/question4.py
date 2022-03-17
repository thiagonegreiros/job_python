# Escreva uma função que receba cinco valores de salários e devolva sua média
def average_wages(wage1, wage2, wage3, wage4, wage5):
    return (wage1 + wage2 + wage3 + wage4 + wage5) / 5


w1 = float(input("Informe o primeiro salario: "))
w2 = float(input("Informe o segundo salario: "))
w3 = float(input("Informe o terceiro salario: "))
w4 = float(input("Informe o quarto salario: "))
w5 = float(input("Informe o quinto salario: "))

avg = average_wages(w1, w2, w3, w4, w5)
print(f"A média entre os salarios é: {avg}")
