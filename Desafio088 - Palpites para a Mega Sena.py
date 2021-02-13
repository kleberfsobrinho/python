from random import randint
from time import sleep
quant = int(input('Quantos jogos serão sorteados? '))
palpites = list()
jogo = list()
tam = 0
while tam < quant:
    for c in range(0, 6):
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    palpites.append(jogo[:])
    jogo.clear()
    tam += 1
tam = 0
print(f'{"SORTEANDO JOGOS":=^35}')
while tam < quant:
    palpites[tam].sort()
    print(f'Jogo {tam + 1} - {palpites[tam]}')
    sleep(1)
    tam += 1
print(f'{"BOA SORTE":=^35}')
