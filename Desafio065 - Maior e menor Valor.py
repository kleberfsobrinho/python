num = float(input('Entre com um número: '))
media = maior = menor = num
cont = 1
op = str(input('Quer continuar [ S/N ]: ')).strip().upper()
if op == 'S':
    while op == 'S':
        num = float(input('Entre com o novo número: '))
        media += num
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        cont += 1
        op = str(input('Deseja continuar[ S/N ]? ')).strip().upper()[0]
else:
    quit()
print('Quantidade de números digitados: {}'.format(cont))
print('Média: {}'.format(media/cont))
print('Maior: {}'.format(maior))
print(('Menor: {}'.format(menor)))
