velo = float(input('Digite a velocidade: '))
if velo > 80:
    acima = (velo - 80)*7

if velo > 80:
    print('Você está acima da velocidade permitida,a velocidade máxima permitida é 80KM/H '
          'e você estava a {:.1f}KM/H. Você receberá uma multa de R${:.1f}'.format(velo, acima))
else:
    print('Você esta dentro da velocidade permitida, boa viagem!')


