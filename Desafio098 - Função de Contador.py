from time import sleep


def contador(inicio, fim, passo):
    f = fim
    p = passo
    if p < 0:
        p *= -1
    elif p == 0:
        p = 1
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo *= -1
    if fim < inicio:
        passo *= -1
        fim -= 2
    print(f'-' * 40)
    print(f'Contagem de {inicio} até {f} de {p} em {p}')
    for c in range(inicio, fim + 1, passo):
        print(f'{c} ', end='', flush=True)
        sleep(0.3)
    print()


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print(f'-' * 40)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Ínicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
