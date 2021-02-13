from datetime import date
ano = int(input('Entre com o ano: '))
if ano == 0:
    ano = date.today().year
if ano%4 == 0:
    if ano % 100 == 0 and ano % 400 != 0:
        print('O ano {} não é bissexto'.format(ano))
    else:
        print('Ano bissexto')
else:
    print('O ano {} não é bissexto'.format(ano))

