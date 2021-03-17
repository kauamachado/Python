tempo = int(input('Quantos anos tem seu carro? '))

print('Seu carro é novo!' if tempo <= 3 else 'carro velho')

if tempo <= 3:
    print('Seu carro é novo')
else:
    print('Seu carro é velho')