valores = int(input('Digite o primeiro valor: ')), int(input('Digite o segundo valor: ')),\
          int(input('Digite o terceiro valor: ')), int(input('Digite o ultimo valor: '))
print(f'Você digitou os valores {valores}')
print(f'O número 9 foi digitado {valores.count(9)} vezes')
if 3 in valores:
    print(f'O número 3 foi digitado pela primeira vez na posição {valores.index(3) + 1}')
else:
    print('O número 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram: ', end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')



