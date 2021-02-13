comprimento1 = float(input('Entre com o comprimento 1: '))
comprimento2 = float(input('Entre com o comprimento 2: '))
comprimento3 = float(input('Entre com o comprimento 3: '))

if comprimento1 < comprimento2 + comprimento3 and comprimento2 < comprimento1 + comprimento3 and comprimento3 < comprimento1 + comprimento2:
    print('Os segmentos podem formar triângulo!')
else:
    print('Os segmentos não formam triângulos!')
