q = 'Desafio 017'
print('{:=^30}'.format(q))
from math import pow #from math import hypot
co = float(input('Entre com o cateto oposto: '))
ca = float(input('Entre com o cateto adjacente: '))
hip = pow(pow(co,2) + pow(ca,2), 0.5) #hypot
print('Hipotenusa = {:.2f}'.format(hip))
from math import hypot
hip1 = hypot(co, ca)
print('Hipotenusa = {:.2f}'.format(hip1))
