sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MF':
    print('Digite uma opção válida. ', end='')
    sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
print('O sexo {} foi registrado com sucesso. '.format(sexo))