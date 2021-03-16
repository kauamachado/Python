from math import hypot
op = float(input('Digite o comprimento do cateto oposto: '))
ad = float(input('Digite o comprimento do cateto adjacente: '))

hip = hypot(op, ad)

print('O comprimento da hipotenusa é {:.2f}'.format(hip))
