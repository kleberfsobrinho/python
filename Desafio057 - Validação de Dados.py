sexo = str(input('Sexo [ M/F ]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Tente novamente: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))


