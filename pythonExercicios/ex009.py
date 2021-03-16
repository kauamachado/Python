print('Challenge 006')
print('Now, lets read the number typed and return double, triple and square root')

value = int(input('Type a number: '))
double = value * 2
triple = value * 3
square = value ** (1/2)

print('Double {} is {}, triple is {} and square root is {:.2f}'.format(value, double, triple, square))
