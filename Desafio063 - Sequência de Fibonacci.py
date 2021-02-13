n = int(input('Entre com o valor de n: '))
num = 0
num1 = 1
cont = 2
print('{} -> {} -> '.format(num, num1), end='')
while cont != n:
    num2 = num + num1
    print('{} -> '.format(num2), end='')
    num = num1
    num1 = num2
    cont += 1
print('FIM')
