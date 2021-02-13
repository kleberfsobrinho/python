from random import randint
from time import sleep
from operator import itemgetter
jogadores = dict()
jogadores['jogador1'] = randint(1, 6)       #jogo = {'jogador1' : randint(1, 6), 'jogador2' : randint(1, 6), 'jogador3' : randint(1, 6), 'jogador4' : randint(1, 6), }
jogadores['jogador2'] = randint(1, 6)
jogadores['jogador3'] = randint(1, 6)
jogadores['jogador4'] = randint(1, 6)
ranking = list() #or dict()
print('Valores sorteados: ')
for k, v in jogadores.items():
    print(f'{k} tirou {v}')
    sleep(0.5)
print()
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}')
    sleep(0.5)
