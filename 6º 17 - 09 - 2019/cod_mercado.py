quantidade = 0
soma=0
while True:
    cod = int(input('Digite codigo: '))
    numero = int(input('Digite 0 para parar: '))
    if numero == 0:
        break
    elif cod == 1:
        oper = 0.50
    elif cod == 2:
        oper = 1
    elif cod == 3:
        oper = 4
    elif cod == 5:
        oper = 7
    elif cod == 9:
        oper = 8
        quantidade = int(input('Digite quantidade: '))
        soma=soma+(oper*quantidade)
        print(soma)
else:    
            print('Codigo invalido')
            quantidade = quantidade + 1
 
