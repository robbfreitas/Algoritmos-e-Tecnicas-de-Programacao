nota = float(input('Digite nota: '))
if nota>=9 and nota <=10:
    print('A')
elif nota>=8 and nota<9:
    print('B')
elif nota>=7 and nota <8:
    print('C')
elif nota<7 and nota>0:
    print('E')
elif nota<0:
    print('Invalido')
elif nota>10:
    print('Invalido')
