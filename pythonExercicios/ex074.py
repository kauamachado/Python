soma = cont =0
while True:
    num = int(input('Digite um número (999 pra parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}!')