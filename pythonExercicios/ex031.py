n = str(input('Digite seu nome completo: ')).strip().title()
nome = n.split()

print('Prazer\nSeu primeiro nome é: {}'.format((nome[0])),
      '\nE seu ultimo nome é: {}'.format(nome[len(nome)-1]))
