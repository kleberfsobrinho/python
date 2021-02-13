tupla_num = ('zero', 'um', 'dois', 'três', 'quatro',
             'cinco', 'sex', 'sete', 'oito', 'nove',
             'dez', 'onze', 'doze', 'treze', 'catorze',
             'quinze', 'dezesseis', 'dezessete', 'dezoito',
             'dezenove', 'vinte')
while True:
    num = int(input('Entre com um número [0 - 20]: '))
    if 0 <= num <= 20:
        break
print(f'Você digitou {tupla_num[num]}')
