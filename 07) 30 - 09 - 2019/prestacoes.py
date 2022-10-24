valor = int(input('Digite valor da compra: '))
for i in range(1, 21):
    print(('{} x de {} reais'.format(i, valor//i)))
    
