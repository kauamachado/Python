n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
med = (n1 + n2)/2

if med < 5:
    print('Reprovado. A média foi: {:.1f}'.format(med))
elif med == 5 or med <= 6.9:
    print('Recuperação. A média foi: {:.1f}'.format(med))
elif med >= 7:
    print('Aprovado. Média: {}'.format(med))