dados = dict()
grupo = list()
soma_idades = 0
while True:
    dados['Nome'] = str(input('Nome: '))
    sexo = str(input('Sexo: [M/F] ')).upper()[0]
    if sexo not in 'MmFf':
        while True:
            sexo = str(input('Tente novamente. Sexo: [M/F] ')).upper()[0]
            if sexo in 'MF':
                break
    dados['Sexo'] = sexo
    dados['Idade'] = int(input('Idade: '))
    soma_idades += dados['Idade']
    grupo.append(dados.copy())
    opcao = str(input('Deseja continuar? [S/N] '))
    if opcao in 'Nn':
        break
    elif opcao not in 'Ss':
        while True:
            opcao = str(input('Tente novamente. Deseja continuar? [S/N] '))
            if opcao in 'Nn':
                break
        if opcao in 'Nn':
            break
print()
print(f'Um total de {len(grupo)} pessoas foram cadastradas.')
media = soma_idades / len(grupo)
print(f'A média das idades é de {media:.2f} anos.')
print()
print('Mulheres cadastradas: ')
for i in grupo:
    if i["Sexo"] in 'Ff':
        print(f'{i["Nome"]} - {i["Idade"]} anos')
print()
print('Pessoas cadastradas acima da média de idades: : ')
for i in grupo:
    if i["Idade"] > media:
        print(f'{i["Nome"]} - [{i["Sexo"]}] - {i["Idade"]} anos')
