cores = {'limpa':'\033[m','verde':'\033[32m','vermelho':'\033[31m','pretoebranco':'\033[1;7;30m'}

nota1 = float(input('Entre com a primeira nota: '))
nota2 = float(input('Entre com a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('{}REPROVADO{}'.format(cores['vermelho'],cores['limpa']))
elif media < 7:
    print('{}RECUPERAÇÃO{}'.format(cores['pretoebranco'],cores['limpa']))
else:
    print('{}APROVADO{}'.format(cores['verde'],cores['limpa']))
