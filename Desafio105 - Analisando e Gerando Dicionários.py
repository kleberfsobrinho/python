def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com informações da turma.
    """
    boletim = dict()
    boletim['total'] = len(n)
    boletim['maior'] = max(n)
    boletim['menor'] = min(n)
    boletim['média'] = sum(n)/len(n)
    if sit:
        if 8 >= boletim['média'] >= 7:
            boletim['situação'] = 'BOA'
        elif boletim['média'] > 8:
            boletim['situação'] = 'ÓTIMA'
        elif 5 <= boletim['média'] < 7:
            boletim['situação'] = 'RAZOÁVEL'
        elif boletim['média'] < 5:
            boletim['situação'] = 'RUIM'
    return boletim


# Programa Principal
resp = notas(5.5, 10, 8, sit=True)
print(resp)
