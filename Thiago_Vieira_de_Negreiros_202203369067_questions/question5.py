# Escrever uma função que receba X e Y e devolva o MDC entre eles
def mdc(x, y):
    while(y != 0):
        rest = x % y
        x = y
        y = rest

    return x


x = int(input("Informe o primeiro valor: "))
y = int(input("Informe o segundo valor: "))
result = mdc(x, y)
print(f"O Máximo Divisor Comum MDC({x},{y}) = {result}")
