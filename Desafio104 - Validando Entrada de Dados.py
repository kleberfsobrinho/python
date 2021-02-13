def leiaInt(st):
    while True:
        n = str(input(f'{st}')).strip()
        if n.isnumeric():
            break
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
    return n

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
