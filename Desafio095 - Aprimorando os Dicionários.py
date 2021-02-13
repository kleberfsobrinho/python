grupo = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))
    quant_partidas = int(input(f'Quantidade de partidas jogadas por {jogador["nome"]}: '))
    partidas.clear()
    for c in range(0, quant_partidas):
        partidas.append(int(input(f'Quantidade de gols na {c + 1}ª partida: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    grupo.append(jogador.copy())
    while True:
        opcao = str(input('Deseja continuar? [S/N] '))
        if opcao in 'SsNn':
            break
        print('Tente Novamente. ', end='')
    if opcao in 'Nn':
        break
print(f'{"cod":>4} {"Nome":<15}{"Gols":<15}{"Total":<5}')

'''print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()'''

for i, v in enumerate(grupo):
    print(f'{i:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 interrompe) '))
    if busca == 999:
        break
    elif busca >= len(grupo):
        print(f'Não existe um jogador com este código.')
    else:
        print(F' == LEVANTAMENTO DO JOGADOR {grupo[busca]["nome"]} == ')
        for i, g in enumerate(grupo[busca]['gols']):
            print(f'Partida {i + 1} - {g} gols')
