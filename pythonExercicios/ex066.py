valor1 = int(input('Digite o 1º valor: '))
valor2 = int(input('Digite o 2º valor: '))
opc = 0
while opc != 5:
    print('''    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos números
    [5]Sair do programa
    ''')
    escolha = str(input('Qual sua opção? '))

    if escolha in '1':
        total = valor1 + valor2
        print('{} + {} é igual a {}'.format(valor1, valor2, total))
    if escolha in '2':
        total = valor1 * valor2
        print('{} * {} é igual a {}'.format(valor1, valor2, total))
    if escolha in '3':
        maior = max(valor1, valor2)
        print('O maior valor entre {} e {} é {}'.format(valor1, valor2, maior))
    if escolha in '4':
        valor1 = int(input('Digite o 1º valor: '))
        valor2 = int(input('Digite o 2º valor: '))

        print('''    [1]Somar
        [2]Multiplicar
        [3]Maior
        [4]Novos números
        [5]Sair do programa
        ''')
        escolha = str(input('Qual sua opção? '))

        if escolha in '1':
            total = valor1 + valor2
            print('{} + {} é igual a {}'.format(valor1, valor2, total))
        if escolha in '2':
            total = valor1 * valor2
            print('{} * {} é igual a {}'.format(valor1, valor2, total))
        if escolha in '3':
            maior = max(valor1, valor2)
            print('O maior valor entre {} e {} é {}'.format(valor1, valor2, maior))
    while escolha > '5' or escolha < '1' or escolha == '5':
        print('Tchau')
        exit()