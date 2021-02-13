s = c = 0
while True:
    num = int(input('Digite o número: '))
    if num == 999:
        break
    s += num
    c += 1
print(f'A soma dos {c} valores foi {s}!')
