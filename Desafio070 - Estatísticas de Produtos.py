m_barato = nome = ''
soma = cont = m_mil = 0
while True:
    produto = str(input('Nome do produto: ')).strip().capitalize()
    preço = float(input('Preço: '))
    cont += 1
    soma += preço
    if cont == 1:
        m_barato = preço
        nome = produto
    if preço < m_barato:
         nome = produto
    if preço > 1000:
        m_mil += 1
    op = ' '
    while op not in 'SsNn':
        op = str(input('Deseja continuar? [ S/N ] ')).strip().upper()[0]
    if op == 'N':
        break
print(f'Total gasto: {soma}')
print(f'Mais de mil {m_mil} produtos')
print(f'{nome} é o produto mais barato!')
