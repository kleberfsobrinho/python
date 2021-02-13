pessoas = list()
dado = list()
mai = men = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    opcao = str(input('Deseja continuar? [S/N] '))
    if opcao in 'Nn':
        break
print(f'{len(pessoas)} pessoas foram cadastradas!')
print(f'Maior peso {mai} ', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'Menor peso {men} ', end='')
for p in pessoas:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
