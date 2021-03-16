print('===Challenge 010===')

print('In this program wee will take the amount you have in the wallet, and inform how many dollars you can buy')

value = float(input('Enter the amount you have in your wallet:R$ '))

dolar = value / 5.63
euro = value / 6.71

print('You have {} reals in your wallet, you can buy {:.2f} dollars and {:.2f}'.format(value, dolar, euro))
