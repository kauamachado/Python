print('===Challenge 005===')
print('Next, enter two numbers and we will show your successor, and your predecessor')

number = int(input('Enter a number: '))
pred = number - 1
suc = number + 1
print('The predecessor of {} is {} and the successor is {}'.format(number, pred, suc))

#Se a variavel so for usada uma vez, o código tbm pode ser: number = int(input('Digite um numero'))
#print('O antecessor de {} é {} e seu sucessor é {}'.format(number, (number-1), (number+1)))