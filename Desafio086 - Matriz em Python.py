matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
valor = 0
for a in range(0, 3):
    for b in range(0, 3):
        matriz[a][b] = (int(input(f'Digite um valor para [{a}, {b}]: ')))
for a in range(0, 3):
    for b in range(0, 3):
        print(f'[{matriz[a][b]:^7}]', end='')
    print()
