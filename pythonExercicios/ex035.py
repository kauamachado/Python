import random
from time import sleep
tentativa = 3
sorteado = random.randint(0, 5)

user = int(input('Digite o número que o computador sorteou: '))

if user > 5 or user < 0:
    print('Digite um número válido!')
    exit()
print('PROCESSANDO....')
sleep(3)
if sorteado == user:
    print('Número sorteado:{}\nVocê venceu!'.format(sorteado))
else:
    print('Número sorteado: {}\nComputador venceu!'.format(sorteado))
