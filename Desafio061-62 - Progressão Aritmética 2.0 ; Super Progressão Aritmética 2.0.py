p_termo = float(input('Entre o primeiro termo: '))
razão = float(input('Entre com a razão: '))
q_termos = 10
termo = p_termo
c = 0
while termo != p_termo + (q_termos) * razão:
    print('{} '.format(termo), end='')
    termo += razão
op = str(input('\nDeseja mostrar mais termos [ S/N ]: '))
if op in 'Ss':
    while q_termos != 0:
        q_termos = int(input('Quantos termos: '))
        while termo != p_termo + (q_termos) * razão:
            print('{} '.format(termo), end='')
            termo += razão
else:
    quit()
