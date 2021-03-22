nome = str(input('Qual é seu nome? ')).lower().strip()
if nome == 'kaua' or nome == 'kauã':
    print('Que nome lindo você tem, Kauã! ')
elif nome == 'daniel':
    print('Seu nome é top, Daniel')
elif nome in 'maria julia augusta':
    print('Nome padrao hein')
else:
    print('Que nome sem graça, {}'.format(nome.title()))
print('\033[1;35;40mTenha um bom dia, {}!\033[m'.format(nome.title()))