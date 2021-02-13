matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_p = soma_c = maior = 0
for a in range(0, 3):
    for b in range(0, 3):
        matriz[a][b] = (int(input(f'Digite um valor para [{a}, {b}]: ')))
for a in range(0, 3):
    for b in range(0, 3):
        print(f'[{matriz[a][b]:^7}]', end='')
        if matriz[a][b] % 2 == 0:
            soma_p += matriz[a][b]
        if a == 1:
            if matriz[1][b] > maior:
                maior = matriz[1][b]
    soma_c += matriz[a][2]
    print()
print(f'Soma dos pares: {soma_p}')
print(f'Soma dos valores 3ª coluna: {soma_c}')
print(f'Maior coluna 2: {maior}')
