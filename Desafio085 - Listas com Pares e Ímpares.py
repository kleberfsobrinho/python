v = [[], []]
valor = 0
for c in range(0, 7):
    valor = int(input(f'Entre com o {c+1}º valor: '))
    if valor % 2 == 0:
        v[0].append(valor)
    else:
        v[1].append(valor)
v[0].sort()
v[1].sort()
print(f'Os pares foram: {v[0]}')
print(f'Os ímpares foram: {v[1]}')
