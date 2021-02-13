salario = float(input('Entre com o valor do salário: '))
if salario > 1250.00:
    salario = salario + salario*0.1
else:
    salario = salario + salario*0.15
print('Novo salário: {:.2f}'.format(salario))
