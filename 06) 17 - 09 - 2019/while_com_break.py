soma = 0
while True:
    numero = int(input('Digite um número a somar ou 0 para sair: '))
    if numero == 0:
        break
    soma = soma + numero
print('A soma dos números é {}'.format(soma))
