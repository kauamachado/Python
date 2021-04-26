i = int(input('Primeiro termo: '))
p = int(input('Razão: '))
n = 10
f = i + (n - 1) * p
f = f + 1

for c in range(i, f, p):
    print(c)
print('Fim')
