from time import sleep


def maior(*num):
    m = tam = 0
    print('-' * 70)
    print('Analisando os valores passados...')
    for c in num:
        print(f'[{c}] ', end='', flush=True)
        sleep(0.2)
        if tam == 0:
            m = c
        elif c > m:
            m = c
        tam += 1
    print(f'O maior valor informado foi: {m} dos {tam} informados')
    sleep(0.4)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
