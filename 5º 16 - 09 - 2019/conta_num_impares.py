fim = int(input('Informe ultimo numero a imprimir: '))
x = 0
cont = 0
while x <= fim:
    if x % 2 != 0:
        print(x)
        cont = cont + 1
    x = x + 1
print('Foram escritos {} numeros'.format(cont))
