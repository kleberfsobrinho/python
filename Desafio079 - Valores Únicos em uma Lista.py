lista = []
while True:
    valor = int(input('Valor: '))
    if valor in lista:                  #not in
        print('Valor já adicionado')
    else:
        lista.append(valor)
    opcao = str(input('Deseja continuar? [S/N] '))
    if opcao in 'Nn':
        break
print()
lista.sort()
print(f'Valores digitador {lista}')
