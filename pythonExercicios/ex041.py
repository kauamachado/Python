salario = float(input('Digite seu salário: '))
n1 = (salario * 15)/100
n2 = (salario * 10)/100
val = salario + n1
if salario >= 1250:
    val = salario + n2
print('Seu salário de R${:.2f}'
      ' passou para:{:.2f}'.format(salario, val))
