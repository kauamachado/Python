valor = float(input('Digite o valor do produto: '))

vista = valor - (valor * 26 / 100)
prazo = valor + (valor * 8 / 100)

print('O valor do produto é {}, se for pago a vista tem um desconto de 26%, ficando R${}. E se for a prazo, um aumento de '
      '8%, ficando {}'.format(valor, vista, prazo))