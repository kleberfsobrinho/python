print('=' * 35)
print('{:^35}'.format('BANCO PYTHON'))
print('=' * 35)
valor = int(input('Que valor você quer sacar? R$ '))
q50 = q20 = q10 = q1 = 0
while True:
    if valor >= 50:
        q50 += 1
        valor -= 50
    elif valor >= 20:
        q20 += 1
        valor -= 20
    elif valor >= 10:
        q10 += 1
        valor -= 10
    elif valor >= 1:
        q1 += 1
        valor -= 1
    if valor == 0:
        break
if q1 != 0:
    print(f'Total de {q1} notas de R$ 1')
if q10 != 0:
    print(f'Total de {q10} notas de R$ 10')
if q20 != 0:
    print(f'Total de {q20} notas de R$ 20')
if q50 != 0:
    print(f'Total de {q50} notas de R$ 50')
print('=' * 35)

