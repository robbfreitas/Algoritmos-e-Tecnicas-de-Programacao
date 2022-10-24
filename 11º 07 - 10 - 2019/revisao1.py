x = 0
soma = 0
lista = []
while x < 5:
    nota = float(input('Digite nota {}: '.format(x+1)))
    lista.append(nota)
    soma += nota
    x += 1
print(lista)
print('Soma: ', soma)
print('Media: ', soma/5)
