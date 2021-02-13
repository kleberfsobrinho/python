q = 'Desafio 022'
print('{:=^20}'.format(q))

nome = str(input('Digite nome: ')).strip()
print('LM: {}'.format(nome.upper()))
print('lm: {}'.format(nome.lower()))
print('Nome sem espações: {}'.format(len(nome)-nome.count(' ')))
dividido = nome.split()
print('Primeiro nome: {}'.format(len(dividido[0]))) #.format(nome.find(' '))
