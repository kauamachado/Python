lista = ('Lápis', 1.75, 'Borracha', 0.50, 'Caneta', 3.25, 'Lapiseira', 2.94, 'Bolsinha', 8.40)
print('-' * 30)
print('LISTAGEM DE PREÇOS')
print('-' * 30)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>5.2f}')