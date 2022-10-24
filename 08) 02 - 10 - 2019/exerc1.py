num = int(input('Entre com numero: '))
num2 = int(input('Enter com segundo numero: '))

def maior(num, num2):
    if num > num2:
        return num
    else:
        return num2

def multiplo(num,num2):
    if num % num2 == 0:
        return True
    else:
        return False
print('O maior é ', maior(num,num2))
print('Multiplo ', multiplo(num,num2))
