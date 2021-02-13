contador = 0
c2 = 0
media = 0
m_idade = 0
for c in range(0, 4):
    nome = str(input('{}º Nome: '.format(contador + 1))).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip().upper()
    if c >= 0:
        print('\n')
    contador += 1
    media += idade
    if sexo == 'MASCULINO':
        if idade > m_idade:
            m_idade = idade
            nome_m = nome
    if sexo == 'FEMININO':
        if idade > 20:
            c2 += 1
print('Média: {}'.format(media/4))
print('Mais Velho(HOMEM): {}'.format(nome_m))
print('Acima de 20(MULHERES): {}'.format(c2))

