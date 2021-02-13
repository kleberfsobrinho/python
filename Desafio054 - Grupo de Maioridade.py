from datetime import date
c1 = 0
c2 = 0
for c in range(0,7):
    ano = int(input('{}º Ano: '.format(c1 + 1)))
    ano_atual = date.today().year
    c1 += 1
    if ano_atual - ano >= 21:
        c2 += 1
if c2 == 1:
    print('1 de Maior e 6 de Menor')

else:
    print('Maiores de idade: {} e {} de Menor'.format(c2, 7 - c2))