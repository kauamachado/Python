nome = str(input('Digite seu nome: ')).title().lower()

if nome == 'kaua':
    print('Bom dia, Kauã lindo!!')
else:
    print('Bom dia, {}!'.format(nome))