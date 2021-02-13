'''num1 = int(input('Entre com o 1° valor: '))
num2 = int(input('Entre com o 2° valor: '))
num3 = int(input('Entre com o 3° valor: '))
num4 = int(input('Entre com o 4° valor: '))
tupla_num = (num1, num2, num3, num4)'''

tupla_num = (int(input('Entre com o 1° valor: ')),
             int(input('Entre com o 2° valor: ')),
             int(input('Entre com o 3° valor: ')),
             int(input('Entre com o 4° valor: ')))
if tupla_num.count(9) == 0:
    print(f'O número 9 não apareceu nenhuma vez.')
else:
    print(f'O número 9 apareceu {tupla_num.count(9)} vez(es).')

'''cont = 0
for pos, c in enumerate(tupla_num):
    if c == 3:
        print(f'O primeiro 3 apareceu na {pos + 1}ª posição')
        cont += 1
if cont == 0:
    print(f'Não apareceu 3 na tupla!')'''

if 3 in tupla_num:
    print(f'O primeiro 3 apareceu na {tupla_num.index(3) + 1}ª posição')
else:
    print(f'Não apareceu 3 na tupla!')
print('Número(s) par(es): ', end='')
for par in tupla_num:
    if par % 2 == 0:
        print(f'{par} ', end='')
