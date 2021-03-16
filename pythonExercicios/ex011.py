print('===Challenge 008===')

print('Here we will take a measure in meters and convert to centimeters, and millimeters, respectively')

measure = float(input('Enter a value in meters: '))
km = measure / 1000
hm = measure / 100
dam = measure / 10
dec = measure * 10
cen = measure * 100
mil = measure * 1000


print('{}m\n{}km\n{}hm\n{}dam\n{}dec\n{}cen\n{}mm '.format(measure, km, hm, dam, measure,dec, cen, mil))
