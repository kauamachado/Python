import datetime
ano = int(input('Digite o ano de nascimento: '))
year = datetime.date.today().year
idade = year - ano

if idade <= 9:
    print('Categoria mirim')
elif idade <= 14:
    print('Categoria Infantil')
elif idade <= 19:
    print('Categoria junior')
elif idade == 20:
    print('Categoria senior')
elif idade > 20:
    print('Categoria master')