q = 'Desafio 027'
print('{:=^20}'.format(q))

nome = str(input('Entre com o nome: ')).strip()
dividido = nome.split()
print('Nome completo: {} \nPrimeiro nome: {}\nUltimo nome: {}'.format(nome, dividido[0], dividido[len(dividido)-1]))

