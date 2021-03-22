num = int(input('Digite um número inteiro: '))
e1 = bin(num)[2:]
e2 = oct(num)[2:]
e3 = hex(num)[2:]
escolha = input('Digite o número da sua escolha:\n1-Binários\n2-Octal\n3-Hexadecimal\n')


if escolha == '1':
    print(e1)
elif escolha == '2':
    print(e2)
elif escolha == '3':
    print(e3)
else:
    print('Digite um número entre 1 e 3')
    exit()