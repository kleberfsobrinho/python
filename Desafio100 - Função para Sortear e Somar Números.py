from random import randint


def sorteia(lst):
    for c in range(0, 5):
        lst.append(randint(1, 10))


def somaPar(lst):
    s_P = 0
    for v in lst:
        if v % 2 == 0:
            s_P += v
    print(f'Somando os pares: {s_P}')


numeros = list()
sorteia(numeros)
print(f'Sorteados: {numeros}')
somaPar(numeros)
