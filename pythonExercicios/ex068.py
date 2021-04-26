num = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = num + (10 - 1) * razao

while num < razao+decimo:
    print('{}'.format(num))
    num += razao
print('Tchau')
