from random import randint
comp = randint(0, 10)
jogador = int(input('Digite um inteiro entre 0 e 10: '))
cont = 1
while jogador != comp:
    jogador = int(input('Tente novamente: '))
    cont += 1
print('Parabéns você acertou foram feitas {} tentativa(s)!'.format(cont))
