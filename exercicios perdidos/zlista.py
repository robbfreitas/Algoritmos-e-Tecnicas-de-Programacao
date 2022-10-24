notas=[0,0,0,0,0,0,]
soma=0
x=0
while x <6:
    notas[x]=int(input('digite uma quabtidade de numeros'))
    soma+=notas[x]
    x+=1
print('media:{0}'.format(soma/x))
