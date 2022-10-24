soma = 0
valor_inf = int(input('Digite limite inferior: '))
valor_sup = int(input('Digite limite superior: '))
for i in range (valor_inf, valor_sup + 1):
    soma += i
print(soma)
