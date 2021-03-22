import datetime
ano = int(input('Digite o ano de nascimento: '))
year = datetime.date.today().year
idade = year - ano
tempo = idade - 18
if ano > year or ano < 1900:
    print('Digite um ano válido')
    exit()
if idade > 18:
    saldo = idade - 18
    print('Voce deveria ter se alistado há {} ano(s)'.format(saldo))
    print('Voce tem {} anos. A idade do alistamento já passou. '.format(idade))
    ano = year - saldo
    print('Seu alistamento foi em: {}'.format(ano))

elif idade == 18:
    print('Voce tem {} anos. Se aliste IMEDIATAMENTE'.format(idade))
elif idade < 18:
    saldo = 18 - idade
    print('Ainda falta {} ano(s) para o alistamento'.format(saldo))
    print('Voce tem {} anos. Ainda não é hora de você de se alistar'.format(idade))
    ano = year + saldo
    print('Seu alistamento será em: {}'.format(ano))
