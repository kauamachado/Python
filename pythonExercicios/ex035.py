import random
from time import sleep

al = random.randint(0, 5)

user = int(input('Digite o número que você acha que o computador sorteou: '))

if user > 5 or user < 0:
    print('Digite um número válido!')
    exit()
print('PROCESSANDO....')
sleep(3)
if al == user:
    print('Número sorteado:{}\nVocê venceu!'.format(al))
else:
    print('Número sorteado: {}\nVocê perdeu'.format(al))
