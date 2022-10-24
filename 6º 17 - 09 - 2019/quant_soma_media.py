soma = 0
quantidade = 0
while True:
    numero = int(input('Digite numeros : '))
    if numero == 0:
        break
    soma = soma + numero
    quantidade = quantidade + 1
    media = soma / quantidade
print('A quantidade de numeros digitados {}'.format(quantidade))
print('A soma dos numeros é {}'.format(soma))
print('A media é {}'.format(media))
