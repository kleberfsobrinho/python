lista_t = []    #list()
lista_p = []    #list()
lista_i = []    #list()
while True:
    valor = int(input('Entre com um valor: '))
    lista_t.append(valor)
    if valor % 2 == 0:
        lista_p.append(valor)
    else:
        lista_i.append(valor)
    opcao = str(input('Deseja continuar? [S/N] '))
    if opcao in 'Nn':
        break
print()
print(f'Todos: {lista_t}')
print(f'Pares: {lista_p}')
print(f'Impares: {lista_i}')

'''
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
'''