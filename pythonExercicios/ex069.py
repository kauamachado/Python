num = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = num + (10 - 1) * razao
while num < razao+decimo:
    print('{}'.format(num))
    num += razao
termo = int(input('Quer mostrar mais termos? '))
if termo == 0:
    print('Obrigado!')
    exit()
termo = num + (termo - 1) * razao
while num < razao+termo:
    print('{}'.format(num))
    num += razao
while termo != 0:
    while num < razao + decimo:
        print('{}'.format(num))
        num += razao
    termo = int(input('Quer mostrar mais termos? '))
    if termo == 0:
        print('Obrigado!')
        exit()
    termo = num + (termo - 1) * razao
    while num < razao + termo:
        print('{}'.format(num))
        num += razao
print('Tchau')
