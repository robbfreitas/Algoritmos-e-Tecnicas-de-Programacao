peso = float(input('Informe o peso em kg: '))
altura = float(input('Informe a altura em metros: '))
imc = peso/(altura*altura)
print('IMC é {}'.format(imc))
if imc<18.5:
    print('Adulto com baixo peso')
elif imc>=18.5 and imc <25:
          print('Adulto com peso adequado')
elif imc>=25 and imc <30:
          print('Adulto com sobrepeso')
elif imc>=30:
          print('Adulto com obesidade')
          
