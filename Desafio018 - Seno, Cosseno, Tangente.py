q = 'Desafio 018'
print('{:=^20}'.format(q))
from math import cos, sin, tan, radians
ang = float(input('Entre com o ângulo em graus: '))
rad = radians(ang)
print('Seno = {:.2f} \nCosseno = {:.2f} \nTangente = {:.2f}'.format(sin(rad), cos(rad), tan(rad)))


