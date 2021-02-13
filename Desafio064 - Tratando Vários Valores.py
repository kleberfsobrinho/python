num = int(input('Entre com o inteiro: '))
soma = cont = 0
while num != 999:
    soma += num
    cont += 1
    num = int(input('Entre com o inteiro: '))
print('Foram digitados {} números!'.format(cont))
print('Soma = {}'.format(soma))
