print('===Challenge 011===')
print('This program will read the width and height of a wall, calculating its area and amount os paint needed'
      'to paint it, considering that a can os paint paint 2m²')

w = float(input('Enter the width: '))
h = float(input('Enter the height: '))
area = (w *h)
nec = area / 2

print('The area between {} x {} is {:.2f}m². And the amount of paint cans required'
      'to paint this wall is {:.2f} lts'.format(w, h, area, nec))