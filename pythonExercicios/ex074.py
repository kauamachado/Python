s = 0
cont = 0
num = int(input('Digite um número: [999 para parar]'))
while True:
    cont += 1
    s += num
    num = int(input('Digite um número: [999 para parar]'))
    if num == 999:
        print(f'A soma dos {cont} valores foi {s}!')
        break
