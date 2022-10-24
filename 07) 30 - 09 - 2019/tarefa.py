x = 1
lista = []
while x <= 10:
    lista.append(x)
    x += 1
print(lista)
lista.pop(2)
print(lista)
lista.remove(5)
print(lista)
lista.append(11)
print(lista)
lista.append(12)
print(lista)
lista.insert(0,0)
print(lista)
print(len(lista))
lista.insert(2,10)
print(lista)
lista_2 = [1, 2, 10, 5, 20]
print('nova lista', lista_2)
print(lista_2.index(10))
