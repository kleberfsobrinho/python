import emoji
from time import sleep
cores = {'limpa':'\033[m', 'branco':'\033[1;30m'}
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize('{}ANO NOVO{}!!! :boom:'.format(cores['branco'], cores['limpa']), use_aliases=True))

