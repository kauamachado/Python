from random import shuffle

g1 = input('Digite o nome do aluno representante do grupo A: ')
g2 = input('Digite o nome do aluno representante do grupo B: ')
g3 = input('Digite o nome do aluno representante do grupo C: ')
g4 = input('Digite o nome do aluno representante do grupo D: ')
lista = [g1, g2, g3, g4]
shuffle(lista)

print('A ordem de apresentação será: ')
print(lista)
