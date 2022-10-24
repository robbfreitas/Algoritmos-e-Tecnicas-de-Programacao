def maximo (a,b):
    if a > b:
        return a
    else:
        return b
def multiplo (x,y):
    if x % y == 0:
        return True
    else:
        return False
num1 = int(input('Numero 1: '))
num2 = int(input('Numero 2: '))

print('Maximo: ', maximo(num1,num2))
print('Multiplo: ', multiplo(num1,num2))
