maior = 0
menor = 0
for c in range(0, 5):
    peso = float(input('{} Peso: '.format(c + 1)))
    if c == 0:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('Maior peso = {} Kg'.format(maior))
print('Menor peso = {} Kg'.format(menor))
