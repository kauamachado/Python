dist = float(input('Digite a distância da viagem: '))
valor = 0.5 * dist

if dist > 200:
    valor = 0.45 * dist

print('A distância da viagem são de {} kilometros e o total a pagar é: {:.1f}'.format(dist, valor))