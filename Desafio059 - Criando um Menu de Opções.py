cores = {'limpa':'\033[m', 'branco':'\033[1;m'}
op = 1
v1 = float(input('Digite o 1º valor: '))
v2 = float(input('Digite o 2º valor: '))
while op != 5:
    print('''[ 1 ]Somar
[ 2 ]Multiplicar
[ 3 ]Maior
[ 4 ]Novos valores
[ 5 ]Sair''')
    op = int(input('Opção: '))
    if op > 5:
        op = int(input('Opção inválida. Tente novamente: '))
    elif op == 1:
        print('Soma = {}{}{}'.format(cores['branco'], v1 + v2, cores['limpa']))
    elif op == 2:
        print('Multiplicação = {}{:.2f}{}'.format(cores['branco'] ,v1 * v2, cores['limpa']))
    elif op == 3:
        maior = v1
        if v2 > v1:
            maior = v2
        print('Maior = {}{}{}'.format(cores['branco'], maior, cores['limpa']))
    elif op == 4:
        v1 = float(input('Digite o NOVO valor 1: '))
        v2 = float(input('Digite o NOVO valor 2: '))
    print('=-=' * 10)
print('Finalizando...')
quit()
