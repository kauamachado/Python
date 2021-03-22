casa = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento: '))

prestacao = casa / (anos * 12)
min = (salario * 30)/100
if prestacao > min:
    print('Para comprar uma casa de R${}, dividido em {} anos, o valor da prestação seria: R${:.2f}. Emprestimo negado'.format(casa, anos, prestacao))
elif prestacao < min:
    print(
        'Para comprar uma casa de R${}, dividido em {} anos, o valor da prestação seria: R${:.2f}. Emprestimo concedido'.format(
            casa, anos, prestacao))