cores = {'limpa':'\033[m', 'verde':'\033[32m', 'vermelho':'\033[31m', 'azul':'\033[34m', 'roxo':'\033[35m', 'amarelo':'\033[33m'}

c1 = float(input('Comprimento 1: '))
c2 = float(input('Comprimento 2: '))
c3 = float(input('Comprimento 3: '))

sub1 = c1 - c2
if sub1 < 0:
    sub1 = sub1*(-1)
sub2 = c1 - c3
if sub2 < 0:
    sub2 = sub2*(-1)
sub3 = c2 - c3
if sub3 < 0:
    sub3 = sub3*(-1)

if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2 and c1 > sub3 and c2 > sub2 and c3 > sub1:
    print('{}FORMA{} triângulo!'.format(cores['verde'], cores['limpa']), end='')
    if c1 == c2 == c3:
        print(' Triângulo {}EQUILATERO{}!'.format(cores['azul'], cores['limpa']))
    elif c1 == c2 or c1 == c3 or c2 == c3:
        print(' Triângulo {}ISOSCELES{}!'.format(cores['roxo'], cores['limpa']))
    else:
        print(' Triângulo {}ESCALENO{}!'.format(cores['amarelo'], cores['limpa']))
else:
    print('{}NÃO FORMA{} triângulo'.format(cores['vermelho'], cores['limpa']))
