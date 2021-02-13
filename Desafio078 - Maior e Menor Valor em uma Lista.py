lista = []
maior = 0
menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite o valor da {c + 1}ª posição: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if maior < lista[c]:
            maior = lista[c]
        if menor > lista[c]:
            menor = lista[c]
print(f'Valores {lista}')
print(f'Maior = {maior} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i + 1} ', end='')
print()
print(f'Menor = {menor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i + 1} ', end='')

