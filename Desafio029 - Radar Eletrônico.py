velocidade = float(input('Entre com a velocidade: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Multado!, {:.2f} R$'.format(multa))
