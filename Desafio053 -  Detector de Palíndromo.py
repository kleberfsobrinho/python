frase = str(input('Frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
#inverso = ''
inverso = junto[::-1]
'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
print('Você digitou: {} e o seu inverso é: {}. Portanto '.format(junto, inverso), end='')
if junto == inverso:
    print('É palindromo!')
else:
    print('NÃO É palindromo!')
