tabela = ('São Paulo', 'America', 'RB Bragantino', 'Internacional', 'Chapecoense', 'Athletico Pr', 'Bahia', 'Ceará', 'Fortaleza',
          'Atl. Goianiense', 'Atl Mineiro', 'Cuiaba', 'Fluminense', 'Juventude', 'Sport', 'Gremio', 'Flamengo','Santos', 'Palmeiras',
          'Corinthians')
print(f'Classificação final:{tabela} ')
print('-'* 280)
print(f'O {tabela[0]} foi campeão e o {tabela[1]} vice.')
print('-'* 280)
print(f'Os 5 primeiros colocados são {tabela[:5]}')
print('-'* 280)
print(f'Os 4 ultimos colocados são {tabela[16:]}')
print('-'* 280)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-'* 280)
print(f'A chapecoense na {tabela.index("Chapecoense")+ 1}ª posicao')
print('-'* 280)
