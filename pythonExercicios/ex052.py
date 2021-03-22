from random import randint
from time import sleep

lista = ('Pedra', 'Papel', 'Tesoura')

pc = randint(0, 2)

perg = int(input('''Escolha uma opção:
[0]Pedra
[1]Papel
[2]Tesoura
'''))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

print('=-' * 20)
print('O computador escolheu: {}'.format(lista[pc]))
print('O jogador escolheu escolheu: {}'.format(lista[perg]))
print('=-' * 20)
if pc == 0:
    if perg == 0:
        print('Empate')
    elif perg == 1:
        print('Jogador venceu')
    elif perg == 2:
        print('Jogador perdeu')
if pc == 1:
    if perg == 0:
        print('Jogador perdeu')
    elif perg == 1:
        print('Empate')
    elif perg == 2:
        print('Jogador venceu')
if pc == 2:
    if perg == 0:
        print('Jogador venceu')
    elif perg == 1:
        print('Jogador venceu')
    elif perg == 2:
        print('Empate')
