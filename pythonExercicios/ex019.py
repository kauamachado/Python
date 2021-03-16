dias = int(input('Quantos dias voce ficou com o carro? '))
km = float(input('Quantos Km voce rodou? '))

tot = (dias * 60) + (km * 0.15)

print('Voce ficou {} dias com o carro, e rodou {} kilometros. O total a se pagar é R${:.2f}'.format(dias, km, tot))
