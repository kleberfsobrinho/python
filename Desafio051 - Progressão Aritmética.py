contador = 0
p_termo = int(input('Primeiro termo: '))
razao = int(input('Razão PA: '))
q_termos = 10
for c in range(p_termo, (p_termo + q_termos * razao), razao):
    print('{}º Termo = {}'.format(contador + 1, c))
    contador += 1
