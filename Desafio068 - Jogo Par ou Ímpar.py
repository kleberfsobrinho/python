from random import randint
cores = {'limpa':'\033[m', 'verde':'\033[32m', 'vermelho':'\033[31m'}
c = randint(0,10)
cn = 0
while True:
    print('-' * 25)
    print('''[ 1 ] Par 
[ 2 ] Impar''')
    e_j = int(input('Entre com sua opção: '))
    while e_j != 1 and e_j != 2:
        e_j = int(input('Opção inválida. Tente novamente: '))
    j = int(input('Entre com o seu valor: '))
    if e_j == 1:
        if (j + c) % 2 == 0:
            print(f'Jogador entrou com {j} e o computador com {c}')
            print('Jogador {}venceu{}!'.format(cores['verde'], cores['limpa']))
            cn += 1
        else:
            print(f'Jogador entrou com {j} e o computador com {c}')
            print('Jogador {}perdeu{}!'.format(cores['vermelho'], cores['limpa']))
            break
    else:
        if (j + c) % 2 == 0:
            print(f'Jogador entrou com {j} e o computador com {c}')
            print('Jogador {}perdeu{}!'.format(cores['vermelho'], cores['limpa']))
            break
        else:
            print(f'Jogador entrou com {j} e o computador com {c}')
            print('Jogador {}venceu{}!'.format(cores['verde'], cores['limpa']))
            cn += 1
if c == 1:
    print('\nJogador venceu uma vez')
else:
    print(f'\nJogador venceu {cn} vezes')
