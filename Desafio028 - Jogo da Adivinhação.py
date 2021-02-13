import random
from time import sleep
num = random.randint(0,5)
n = int(input('Escolha um número de 0 a 5: '))
sleep(3)
if n == num:
    print('Parabens, você venceu!')
else:
    print('O computador venceu! O número era: {}'.format(num))