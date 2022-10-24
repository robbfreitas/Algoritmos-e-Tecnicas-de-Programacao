numeros = []
soma = 0
for i in range (5):
    numero = int(input('Entre com um numero {}: '.format(i+1)))
    numeros.append(numero)
    if numero % 2 != 0:
        soma += numero
print(numeros)
print('Soma: ', soma)
