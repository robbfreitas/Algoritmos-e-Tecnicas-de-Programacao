fim = int(input('apenas pares entre 0 e numero informado aqui: '))
x = 0
while x <= fim:
    if x %2 == 0 and x != 0:
        print(x)
    x = x + 1
