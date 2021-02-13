from datetime import datetime
trabalhador = dict()
trabalhador['Nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
trabalhador['Idade'] = datetime.now().year - ano
trabalhador['Carteira de trabalho'] = int(input('Carteira de trabalho (0 não tem): '))
if trabalhador['Carteira de trabalho'] != 0:
    trabalhador['Ano de contratação'] = int(input('Ano de contratação: '))
    trabalhador['Salário'] = float(input('Salário: R$ '))
    trabalhador['Aposentadoria'] = 35 - (datetime.now().year - trabalhador['Ano de contratação']) + trabalhador['Idade']
for k, v in trabalhador.items():
    print(f'{k} - {v}')
