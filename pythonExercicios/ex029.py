
nome = input('Digite o nome da cidade: ')
nome = nome.lower().split()
rp = 'santo' in nome[0]
print('A cidade começa com Santo no nome: {}'.format(rp))

OU

nome = input('Digite o nome da cidade: ').lower().strip()
print(nome[:5] == 'santo')