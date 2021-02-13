num = int(input('Entre com o valor do número: '))
print('''Escolha uma base:
[ 1 ] Binário 
[ 2 ] Octal 
[ 3 ] Hexadecimal''') #LEMBRAR DAS ''' DENTRO DE PRINTS
op = int(input('Sua opção: '))
if op == 1:
    print('{} convertido para BINÁRIO é {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('{} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!')

