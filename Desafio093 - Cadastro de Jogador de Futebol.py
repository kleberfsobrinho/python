'''jogador = dict()
jogador['Nome'] = str(input('Nome: '))
quant_partidas = int(input(f'Quantidade de partidas {jogador["Nome"]} jogou: '))
total_g = 0
for c in range(0, quant_partidas):
    jogador['Partida {}'.format(c + 1)] = int(input(f'Quantidade de gols na {c + 1}ª partida: '))
    total_g += jogador['Partida {}'.format(c + 1)]
jogador['Total de gols'] = total_g
print()
for k, v in jogador.items():
    print(f'{k} - {v} gols')'''

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome: '))
quant_partidas = int(input(f'Quantidade de partidas {jogador["nome"]} jogou: '))
for c in range(0, quant_partidas):
    partidas.append(int(input(f'Quantidade de gols na {c + 1}ª partida: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print()
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i + 1}, fez {v} gols')
print(f'Um total de {jogador["total"]} gols')
