def escreva(str):
    tam = len(str) + 2
    print('-' * tam)
    print(f' {str} ')
    print('-' * tam)

while True:
    msg = str(input('Entre com a mensagem: ')).strip()
    escreva(msg)
    while True:
        op = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if op in 'SN':
            break
        print('Tente Novamente. ', end='')
    if op in 'N':
        break
