num = int(input('Digite um número: '))
resul = 1
count = 1
while count <= num:
    resul *= count
    count += 1
print('{}!: {}'.format(num, resul))
