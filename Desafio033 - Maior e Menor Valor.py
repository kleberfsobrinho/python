a = float(input('Entre com o número 1: '))
b = float(input('Entre com o número 2: '))
c = float(input('Entre com o número 3: '))

'''if n1 > n2 and n1 > n3:
    if n2 > n3:
        print('O maior número é {} e o menor é {}.'.format(n1,n3))
    else:
        print('O maior número é {} e o menor é {}.'.format(n1, n2))
if n2 > n1 and n2 > n3:
    if n1 > n3:
        print('O maior número é {} e o menor é {}.'.format(n2,n3))
    else:
        print('O maior número é {} e o menor é {}.'.format(n2, n1))
if n3 > n1 and n3 > n2:
    if n1 > n2:
        print('O maior número é {} e o menor é {}.'.format(n3, n2))
    else:
        print('O maior número é {} e o menor é {}.'.format(n3, n1))'''
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor é: {}'.format(menor))
