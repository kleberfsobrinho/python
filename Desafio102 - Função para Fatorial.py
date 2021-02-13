def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: número que será utilizado
    :param show: (opcioal) mostrar ou não a conta
    :return: o fatorial do número escolhido
    """
    f = 1
    print('-' * 30)
    for c in range(num, 0, -1):
        f *= c
    if show:
        for c in range(num, 0, -1):
            if c == 1:
                print(f'{c} = ', end='')
            else:
                print(f'{c} x ', end='')
    return f


# Programa Principal
#help(fatorial)
'''num = int(input('Número para calculo do fatorial: '))
show = int(input('Deseja mostrar o processo de cálculo?\n[ 1 ] - Sim\n[ 2 ] Não\nOpção: '))
if show == 1:
    show = True
else:
    show = False'''
print(fatorial(5, show=True))
