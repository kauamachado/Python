v1 = float(input('Digite o valor da reta 1: '))
v2 = float(input('Digite o valor da reta 2: '))
v3 = float(input('Digite o valor da reta 3: '))
if v1 < v2 + v3 and v2 < v1 + v3 and v3 < v1 + v2:
    print('Os segmentos acima podem formar um triangulo!')
    if v1 == v2 == v3:
        print('Equilatero')
    elif v1 != v2 != v3 != v1:
        print('Escaleno')
    else:
        print('Isosceles')
else:
    print('Não forma um triangulo!')
