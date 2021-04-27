print('--' * 20)
print('CADASTRO DE PESSOAS')
print('--' * 20)
maioridade = 0
homens = 0
mulher = 0
while True:
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('SEXO: [M/F]')).lower().strip()[0]
        if idade >= 18:
            maioridade += 1
        if sexo == 'm':
            homens += 1
        if sexo == 'f' and idade > 20:
            mulher += 1
    escolha = str(input('Quer continuar? [S/N]')).lower().strip()[0]
    while escolha not in 'sn':
        escolha = str(input('Quer continuar? [S/N]')).lower().strip()[0]
    if escolha == 'n':
        print(f'Nesse programa foram cadastradas {maioridade} pessoas com mais de 18 anos. Temos {homens} homens cadastrados. E {mulher} mulher(es) com mais de 20 anos. ')
        break


