print('===Challenge 12===')

print('In this program, we will show the new product value with 5% discount')

valueI = float(input('Enter the value of product: '))
desc = valueI - (valueI * 5/100)

print('The value with discount is {:.2f}'.format(desc))