n1 = int((input('Digite o primeiro número: ')))
if n1 < 0:
    print('Digite um número válido!')
    exit()
n2 = int((input('Digite o segundo número: ')))
if n2 < 0:
    print('Digite um número válido!')
    exit()
n3 = int((input('Digite o terceiro número: ')))
if n3 < 0:
    print('Digite um número válido!')
    exit()

num = n1, n2, n3

print('O maior valor é: {}'.format(max(num)))
print('O menor valor é: {}'.format(min(num)))