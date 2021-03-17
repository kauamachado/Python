num = int(input('Digite um número: '))
if num > 9999 or num < 0:
    print('Digite um número válido!')
    exit()
u = num // 1 % 1
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número: {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))