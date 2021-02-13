from datetime import date
n_ano = int(input('Digite o valor do ano de nascimento: '))
ano = date.today().year
if (ano - n_ano) < 18:
    print('Ainda deverá se alistar faltam {} ano(s)!'.format(18 - (ano - n_ano)))
elif (ano - n_ano) == 18:
    print('É hora de se alistar!')
else:
    print('O tempo de alistamento já passou fazem {} ano(s)!'.format(ano - n_ano - 18))
