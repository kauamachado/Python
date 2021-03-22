produto = float(input('Digite o valor do produto: '))
forma = int(input('Digite a forma de pagamento:\n1- À vista(Dinheiro ou cheque): \n2- À vista no cartão: '
                  '\n3- Duas vezes no cartão: \n4- Três vezes ou mais no cartão: \n'))
esc = str(forma)
f1 = produto - produto * 10 / 100
f2 = produto - produto * 5 / 100
f3 = produto + produto * 20 / 100
if esc <= '0' or esc > '4':
    print('Digite um número entre 1 e 4 para fazer a escolha do pagamento: ')
    exit()

if esc == '1':
    print('A forma escolhida foi à vista(dinheiro ou cheque), o valor de R${:.2f} com desconto ficou: R${:.2f}'.format(produto, f1))
elif esc == '2':
    print('A forma escolhida foi à vista no cartão, o valor de R${:.2f} com desconto ficou: R${:.2f}'.format(produto, f2))
elif esc == '3':
    print('A forma escolhida foi em duas vezes no cartão, o valor é R${:.2f}'.format(produto))
elif esc == '4':
    print('A forma escolhida foi em três ou mais vezes no cartão, o juros nesse caso é de 20%, o valor é R${:.2f}'.format(f3))