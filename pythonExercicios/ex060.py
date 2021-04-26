frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Você digitou {} e o inverso disso é {}.'
          '\nTemos um palindromo'.format(junto, inverso))
else:
    print('Você digitou {} e o inverso disso é {}.'
          '\nNão temos um palindromo'.format(junto, inverso))
