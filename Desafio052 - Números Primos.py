cores = {'limpa':'\033[m', 'verde':'\033[32m', 'vermelho':'\033[31m', 'azul':'\033[1;34m', 'branco':'\033[1;30m'}
contador = 0
num = int(input('Número: '))
print('Divisores:', end='')
for c in range(1, num + 1):
    if num % c == 0:                                    #ideia das cores
        contador += 1
        print('{}'.format(cores['azul']), end='')
    else:
        print('{}'.format(cores['branco']), end='')
    print(' {}'.format(c), end='')
    print('{}'.format(cores['limpa']), end='')
if contador == 2:
    print('\nPortanto {}É{} primo!'.format(cores['verde'], cores['limpa']))
else:
    if num == 0:
        print('\n{}NÃO{} é primo!'.format(cores['vermelho'], cores['limpa']))
    else:
        print('\nPortanto {}NÃO{} é primo!'.format(cores['vermelho'], cores['limpa']))
