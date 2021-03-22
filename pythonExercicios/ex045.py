n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O primeiro valor valor {} é maior que o {}'.format(n1,n2))
elif n1 < n2:
    print('O segundo valor {} é maior que o {}'.format(n2, n1))
elif n1 == n2:
    print('Os valores {} e {} são iguais. '.format(n1, n2))