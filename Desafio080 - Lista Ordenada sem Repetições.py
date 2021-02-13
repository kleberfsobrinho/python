lista = []  #list()
for c in range(0, 5):
    n = int(input('Digite o valor: '))
    if c == 0 or n > lista[len(lista) - 1]: #len(lista) - 1 == -1
        lista.append(n)
        print('Adicionado na última posição')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
        print(f'Adicionado na posição {pos + 1}')
print(f'Os valores digitados em ordem formam {lista}')
