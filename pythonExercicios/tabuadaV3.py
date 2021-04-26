cont = 0
num = int(input('Tabuada de: '))
s = num * cont
while num >= 0:
    cont += 1
    while cont < 11:
        print(f'{num} * {cont} = {num * cont}')
        break
