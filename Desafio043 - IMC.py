cores = {'limpa':'\033[m', 'branco':'\033[1;30m', 'verde':'\033[32m', 'vermelho':'\033[31m', 'azul':'\033[34m', 'amarelo':'\033[33m', 'roxo':'\033[35m'}

peso = float(input('Entre com seu peso em {}KG{}: '.format(cores['branco'], cores['limpa'])))
altura = float(input('Entre com sua altura em {}METROS{}: '.format(cores['branco'], cores['limpa'])))

imc = peso / pow(altura, 2)

print('IMC = {:.2f}'.format(imc))

if imc < 18.5:
    print('{}ABAIXO DO PESO{}'.format(cores['vermelho'], cores['limpa']))
elif imc <= 25:
    print('{}PESO IDEAL{}'.format(cores['verde'], cores['limpa']))
elif imc <= 30:
    print('{}SOBREPESO{}'.format(cores['amarelo'], cores['limpa']))
elif imc <= 40:
    print('{}OBESIDADE{}'.format(cores['azul'], cores['limpa']))
else:
    print('{}OBESIDADE MORBIDA{}'.format(cores['roxo'], cores['limpa']))
