n1 = float(input('Digite a nota da primeira prova: '))
if n1 > 10 or n1 < 0:
    print('Digite uma nota válida!')
    exit()
n2 = float(input('Digite a nota da segunda prova: '))

m = (n1 + n2) /2


if m >= 5:
    print('Parabéns, sua média foi {:.1f} e você foi aprovado!'.format(m))
else:
    print('Estude mais, sua média foi {:.1f} e você foi reprovado!'.format(m))