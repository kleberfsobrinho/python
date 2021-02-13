cores = {'limpa':'\033[m', 'branco':'\33[30m', 'amarelo':'\033[33m', 'azul':'\033[34m', 'roxo':'\033[35m', 'cinza':'\033[37m'}

ano = int(input('Entre com o ano: '))

if ano <= 9:
    print('{}MIRIM{}'.format(cores['branco'], cores['limpa']))
elif ano <= 14:
    print('{}INFANTIL{}'.format(cores['amarelo'], cores['limpa']))
elif ano <= 19:
    print('{}JUNIOR{}'.format(cores['azul'], cores['limpa']))
elif ano <= 20:
    print('{}SÊNIOR{}'.format(cores['roxo'], cores['limpa']))
else:
    print('{}MASTER{}'.format(cores['cinza'], cores['limpa']))
