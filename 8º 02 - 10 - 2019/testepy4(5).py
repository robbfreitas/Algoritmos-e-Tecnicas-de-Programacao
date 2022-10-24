num = int(input('Entre com numero: '))
num2 = int(input('Entre com numero: '))

def par (x):
    return (x % 2 == 0)
def par_impar(y):
    if par (y):
        return 'PAR'
    else:
        return 'IMPAR'

print('O numero {} é: {}'.format(num,par_impar(num)))
print('O numero {} é: {} '.format(num2,par_impar(num2)))
