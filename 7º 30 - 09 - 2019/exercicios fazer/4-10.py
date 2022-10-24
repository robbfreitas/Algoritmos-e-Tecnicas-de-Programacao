soma = 0
a = int(input('Entre com o valor a: '))
b = int(input('Entre com o valor b: '))
n = int(input('Entre com o valor n: '))
for i in range (1, n + 1, b):
    calculo = (a - b*i) + i**2
    soma += calculo
print(soma)
