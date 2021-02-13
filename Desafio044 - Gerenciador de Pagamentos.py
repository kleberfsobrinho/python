'''p_n = float(input('Digite o preço do produto: '))
op = int(input('1 - À vista \n2 - Cartão \nQual a condição de pagamento: '))
if op == 1:
    op2 = int(input('1 - Dinheiro \n2 - Cheque \n3 - Cartão \nQual a opção: '))
    if op2 == 1 or op2 == 2:
        p = p_n - p_n*0.1
    elif op2 == 3:
        p = p_n - p_n*0.05

elif op == 2:
    op2 = int(input('1 - Em 2x \n2 - Em 3 \nQual a opção: '))
    if op2 == 1:
        p = p_n
    elif op2 == 2:
        p = p_n + p_n*0.2

print('\nPreço = {}'.format(p))'''

p = float(input('Entre com o preço do produto: '))
op = str(input('À vista ou parcelado? ')).upper().strip()
print('\n')

if op == 'À VISTA' or op == 'A VISTA':
    op2 = str(input('Dinheiro, cheque ou cartão? ')).upper().strip()
    if op2 == 'DINHEIRO' or op2 == 'CHEQUE':
        n_p = p - p * 0.1
        v = 1
    elif op2 == 'CARTAO' or op2 == 'CARTÃO':
        n_p = p - p * 0.05
        v = 1
    else:
        print('Não apresentamos está opção!')
        v = 0

elif op == 'PARCELADO':
    op2 = str(input('2x no cartão ou 3x no cartão: ')).upper().strip()
    if op2 == '2X' or op2 == '2X NO CARTÃO' or op2 == '2X NO CARTAO':
        n_p = p
        v = 1
    elif op2 == '2X' or op2 == '2X NO CARTÃO' or op2 == '2X NO CARTAO':
        n_p = p + p * 0.2
        v = 1
    else:
        print('Não apresentamos está opção!')
        v = 0

else:
    print('\nNão apresentmaos está opção!')
    v = 0

if v == True:
    print('\nPreço: {}'.format(n_p))
else:
    quit()

