from math import hypot
co = float(input('Qual o cateto oposto em cm?'))
ca = float(input('Qual o cateto adjacente em cm?'))
hi = hypot(co, ca)
print(f'A hipotenusa vale {hi:.2f}cm')
#hip = (co*co) + (ca*ca)
#print(f'A hipotenusa vale:{hip**0.5.:2f}cm')
