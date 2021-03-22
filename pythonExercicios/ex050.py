alt = float(input('Digite sua altura: '))
peso = float(input('Digite o seu peso(m): '))

imc = peso / (alt**2)

if imc < 18.5:
    print('Imc: {:.1f}\nVocê está abaixo do peso.'.format(imc))
elif 18.5 <= imc < 25:
    print('Imc:{:.1f}\nVocê está no peso ideal. '.format(imc))
elif 25 <= imc < 30:
    print('Imc:{:.1f}\nVocê está com sobrepeso. '.format(imc))
elif 30 <= imc < 40:
    print('Imc:{:.1f}\nVocê está obeso. '.format(imc))
elif imc > 40:
    print('Imc:{:.1f}\nVocê está com obesidade morbida. '.format(imc))
