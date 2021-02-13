from random import randint
tupla_num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Sorteados: ', end='')
for c in tupla_num:
    print(f'{c} ', end='')
print(f'\nO maior valor sorteado foi {max(tupla_num)}')
print(f'O menor valor sorteado foi {min(tupla_num)}')
