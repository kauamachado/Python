from random import choice
a1 = input('Digite o nome do 1º aluno: ')
a2 = input('Digite o nome do 2º aluno: ')
a3 = input('Digite o nome do 3° aluno: ')
a4 = input('Digite o nome do 4º aluno: ')
alunos = [a1, a2, a3, a4]

sort = choice(alunos)

print('O aluno sorteado foi: {}'.format(sort))