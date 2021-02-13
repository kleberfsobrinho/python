print('-' * 20)
print('CADASTRO DE PESSOAS!')
print('-' * 20)
q1 = q2 = q3 = 0
c = 1
while True:
    print(f'{c}ª PESSOA ')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [ M/F ]: ')).upper().strip()[0]
    c += 1
    if idade > 18:
        q1 += 1
    if sexo == 'M':
        q2 += 1
    if idade > 20 and sexo == 'F':
        q3 += 1
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar? [ S/N ] ')).upper().strip()[0]
    print('-' * 20)
    if op == 'N':
        break
print(f'{q1} pessoas com mais de 18.')
print(f'{q2} homens cadastrados.')
print(f'{q3} mulheres cadastradas com mais de 20 anos.')