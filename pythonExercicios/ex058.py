s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s = s + c
        cont += 1
print('A SOMA DE TODOS OS {} VALORES  É {}'.format(cont, s))
