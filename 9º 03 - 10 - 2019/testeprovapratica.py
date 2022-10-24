def soma (a,b):
    return a + b
def sub (a,b):
    return a - b
def multi (a,b):
    return a * b
def div (a,b):
    return a / b

num1 = float(input('Informe primeiro número: '))
num2 = float(input('Informe segundo número: '))
print(' 1 - soma\n 2 - sub\n 3 - multi\n 4 - div\n 5 - 0 (parar)')
op = 1
while 0 <= op <= 4:
    op = int(input('Qual operação deseja fazer? '))
    if op == 1:
        print(soma(num1,num2))
    elif op == 2:
        print(sub(num1,num2))
    elif op == 3:
        print(multi(num1,num2))
    elif op == 4:
        print(div(num1,num2))
    elif op == 0:
        break
    else:
        print('Operação inválida')
