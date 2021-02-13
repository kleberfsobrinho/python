cores = {'limpa':'\033[m',
         'verde':'\033[32m',
         'vermelho':'\033[31m',
         'branco':'\033[1;30m',
         'pretoebranco':'\033[1;7;30m'}
import random
from time import sleep
lista = ['Pedra', 'Papel', 'Tesoura']
comp = random.choice(lista)
compu = str(comp).upper()
print('-=' * 14)
usua = str(input('Entre com sua opção: ')).capitalize().strip()
usuar = str(usua).upper()
if usuar != 'PAPEL' and usuar != 'PEDRA' and usuar != 'TESOURA':
    print('\n{}Não há está opção!{}'.format(cores['pretoebranco'], cores['limpa']))
else:
    print('JO')
    sleep(0.8)
    print('KEN')
    sleep(0.8)
    print('PO!!!')
    if compu == 'PEDRA' and usuar == 'PEDRA' or compu == 'PAPEL' and usuar == 'PAPEL' or compu == 'TESOURA' and usuar == 'TESOURA':
      print('\n{}EMPATE{} -> {} = {}'.format(cores['branco'], cores['limpa'], comp, usua))
    elif compu == 'PEDRA' and usuar == 'TESOURA' or compu == 'PAPEL' and usuar == 'PEDRA' or compu == 'TESOURA' and usuar == 'PAPEL':
      print(('\n{}EU VENCI{} -> {} > {}'.format(cores['vermelho'], cores['limpa'], comp, usua)))
    else:
        print('{}\nPARABÉNS{} -> {} > {}'.format(cores['verde'], cores['limpa'], usua, comp))
print('-=' * 14)
