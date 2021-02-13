def voto(ano=0):
    """
    -> Função que recebe o ano de nascimento do usuário e retona sua situação de voto.
    :param ano: ano de nascimento.
    :return: 'VOTO NEGADO' para idade < 18/ 'VOTO OPCIONAL' para idade > 65/ 'VOTO OBRIGATÓRIO' para o intervalo.
    """
    from datetime import datetime
    idade = datetime.now().year - ano
    if idade < 16:
        msg = f'Com {idade} anos: VOTO NEGADO'
    elif idade > 65 and 16 <= idade < 18:
        msg = f'Com {idade} anos: VOTO OPCIONAL'
    else:
        msg = f'Com {idade} anos: VOTO OBRIGATÓRIO'
    return msg


# Programa Principal
ano_nasc = int(input('Nascimento? '))
print(f'{voto(ano_nasc)}')
