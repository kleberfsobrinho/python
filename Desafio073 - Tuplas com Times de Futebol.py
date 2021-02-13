tupla_brasileirao = ('Palmeiras', 'Santos', 'Botafogo', 'Atlético', 'Flamengo', 'Bahia', 'Internacional', 'São Paulo', 'Goiás', 'Corinthias', 'Athletico-PR', 'Ceará SC', 'Grêmio', 'Cruzeiro', 'Fluminense', 'Chapecoense', 'Fortaleza', 'Vasco da Gama', 'CSA', 'Avaí')
print(f'Cinco primeiros colocados: {tupla_brasileirao[:5]}')
print(f'Quatro últimos colocados: {tupla_brasileirao[-4:]}')
print(f'Em ordem alfabética: {sorted(tupla_brasileirao)}')
pos_time = 0

'''for pos, time in enumerate(tupla_brasileirao):
    if time == 'Chapecoense':
        pos_time = pos
print(f'A Chapecoense está na posição: {pos_time + 1}')'''

print(f'A Chapecoense está na posição: {tupla_brasileirao.index("Chapecoense") + 1}')
