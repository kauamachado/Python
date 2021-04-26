
n = 1
soma = 0
while n != 0:
    n = int(input('Digite um número: '))
    soma += n
print('A soma desses valores é: {}'.format(soma))
print('Fim')

c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
    if r != 'S':
        print('Obrigado. ', end='')
print('End.')