nom = input('Escreva uma frase: ').strip().lower().replace(' ', '')
vz = nom.count('a')
fr = nom.find('a')
ult = nom.rfind('a')
print('A letra A aparece: {} vezes\n'.format(vz))
print('Sua primeira posição é na casa: {}\n'.format(fr+1))
print('E sua ultima posição é na casa:{}'.format(ult+1))