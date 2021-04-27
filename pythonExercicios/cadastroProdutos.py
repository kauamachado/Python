print('-' * 20)
print('Loja Super Lojão')
print('-' * 20)
total = caro = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: '))
    cont += 1
    total += preco
    if preco > 1000:
        caro += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    escolha = ' '
    while escolha not in 'sn':
        escolha = str(input('Quer continuar? [S/N]')).lower().strip()[0]
    if escolha == 'n':
        break
print(f'O total da compra foi de R${total:.2f}.'
      f'\nTemos {caro} produtos que custam mais de R$1000 reais.'
      f'\nO produto mais barato foi{barato} que custa R${menor:.2f}')
print('FIM')
