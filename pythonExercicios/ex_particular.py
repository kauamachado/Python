print('Esse programa irá\n '
      'Ler e dizer quantas letras tem seu nome completo e '
      'se tem a letra A nele.\n Vai consultar '
      'se seu nome possui Miranda. '
      '\nPegará o número requisitado e dizer suas unidades, dezena, etc...')

nome = input('Digite seu nome: ').upper().strip().split()
num = int(input('Digite um número: '))
u = num // 1 % 1
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Seu nome é: {}'.format(nome), 'seu primeiro nome tem {} letras.'.format(len(nome[0])))
print('Seu nome possui a letra A: {}'.format('A' in nome[0]))
print('Seu nome tem miranda no meio? {}'.format('MIRANDA' in nome))
print('Analisando o número: {}'.format(num))
print('Unidades: {}'.format(u))
print('Dezenas: {}'.format(d))
print('Centenas: {}'.format(c))
print('Milhares: {}'.format(m))