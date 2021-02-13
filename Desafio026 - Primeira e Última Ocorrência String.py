q = 'Desafio 026'
print('{:=^20}'.format(q))

frase = str(input('Digite uma frase: ')).strip()

print("A's = {}".format(frase.upper().count('A')))
print('1ª vez, Posição = {}'.format(frase.upper().find('A')+1))
print("Último 'A', Posição = {}".format(frase.upper().rfind('A')+1))
