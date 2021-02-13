cores = {'limpa':'\033[m', 'verde':'\033[1;32m', 'vermelho':'\033[31m'}
v_casa = float(input('Entre com o valor da casa: '))
v_salario = float(input('Entre com o valor do salário: '))
n_anos = int(input('Entre com o número de anos: '))
p_mensal = v_casa / n_anos / 12
if p_mensal > 0.3 * v_salario :
    print('\nEmpréstimo de {:.2f} mensal, {}NEGADO{}!'.format(p_mensal, cores['vermelho'],cores['limpa']))
else:
    print('\nEmpréstimo de {:.2f} mensal, {}APROVADO{}!'.format(p_mensal, cores['verde'], cores['limpa']))
