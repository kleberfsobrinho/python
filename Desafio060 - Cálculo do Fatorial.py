num = int(input('Digite um número: '))
fat = 1

if num == 0 or num == 1:       #COM WHILE
    fat = 1
else:
    while num > 0:
        print('{}'.format(num), end='')
        print(' x ' if num > 1 else ' = ', end='')
        fat *= num
        num -= 1
print('{}'.format(fat))

'''for c in range(num, 0, -1):     #COM FOR
    fat *= c
print('Fatorial = {}'.format(fat))'''

'''from math import factorial      #COM MÓDULO 
f = factorial(num)
print('Fatorial = {}'.format(f))'''

