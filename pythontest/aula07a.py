n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n1
su = n1 - n2
di = n1 // n2
e = n1 ** n2

print('A soma entre {} e {} é {}\n'.format(n1, n2, s), 'O produto é {}\nA divisão é {}. '
   '\nEnquanto a subtração vale {}'.format(m, d, su), '\nA divisão  inteira é {} \nE a exponenciação é {}'.format(di, e))
