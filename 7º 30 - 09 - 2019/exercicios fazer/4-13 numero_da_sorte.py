soma = 0
data = int(input('informe a data ddmmaaaa (apenas numeros e juntos): '))
for i in range(0,8):
    resto = data%10
    num2 = data//10
    soma += resto
    data = num2
print('O seu número da sorte é {}'.format(soma))
