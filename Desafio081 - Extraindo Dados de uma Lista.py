lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    opcao = str(input('Deseja continuar? [S/N] '))
    if opcao in 'Nn':
        break
print(f'Foram digitados {len(lista)} valores')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')