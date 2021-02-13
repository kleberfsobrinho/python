c = 1
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        print('Finalizando...')
        print('-' * 20)
        break
    else:
        c = 1
        print('-' * 20)
        while c != 11:
            print(f'{n} x {c} = {c * n}')
            c += 1
        print('-' * 20)
