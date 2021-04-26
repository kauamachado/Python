somaidade = 0 #Soma das idades
mediaid = 0 #Media de todas as idades
maioriahom = 0 #Quantidade de homens maiores de idade
nomevelho = '' #Nome do homem mais velho
totmul = 0 # Total de mulheres menoresd que 20 anos
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()#Strip para retirar os espacos
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioriahom = idade
        nomevelho  = nome
    if sexo in 'Mm' and idade > maioriahom:
        maioriahom = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmul += 1
    mediaid = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaid))
print('O homem mais velho tem {} anos e se chama {}'.format(maioriahom, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmul))