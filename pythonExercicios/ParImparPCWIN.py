from random import randint
print('-=' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 20)
v = 0
while True:
    opc = ' '
    while opc not in 'pi':
        opc = str(input('Você quer par ou impar?[P/I]')).lower().strip()[0]
    jogador = int(input('Digite um valor: '))
    pc = randint(0, 10)
    total = pc + jogador
    print(f'Você jogou {jogador} e o computador jogou {pc}, o total foi {total}', end='')
    print('  Deu par' if total % 2 == 0 else '  Deu impar')
    if opc in 'p':
        if total %2 == 0:
            print('Você ganhou! Vamos seguir')
            v+=1
        else:
            print('Você perdeu. ')
            break
    if opc in 'i':
        if total % 2 == 1:
            print('Você ganhou! Vamos seguir')
        else:
            print('Você perdeu! ')
            break
print(f'FIM. Você venceu {v} vez(es)! ')