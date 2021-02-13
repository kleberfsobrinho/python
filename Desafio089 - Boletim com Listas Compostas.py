aluno = list()
sala = list()
indice = tam = 0
while True:
    aluno.append(indice)
    aluno.append(str(input('Nome: ')))
    nota1 = float(input('Nota 1: '))
    aluno.append(nota1)
    nota2 = float(input('Nota 2: '))
    aluno.append(nota2)
    media = (nota1 + nota2)/2
    aluno.append(media)
    sala.append(aluno[:])           #ficha.append([nome, [nota1, nota2], media])
    aluno.clear()
    opcao = str(input('Deseja continuar? [S/N] '))
    if opcao in 'Nn':
        break
    indice += 1
print()
print(f'{"i":>2} {"Nome":<10} {"Média":<4}')
for i, v in enumerate(sala):
    print(f'{i:>2} {v[1]:<10} {v[4]:>4.2f}')
opcao = 0
print()
while opcao != 999:
    opcao = int(input('Exibir notas de qual aluno: (999 interrompe) '))
    for i, v in enumerate(sala):
        if i == opcao:
            print(f'{v[1]} - Nota 1: {v[2]} - Nota 2: {v[3]}!')
            print()