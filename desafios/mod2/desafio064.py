quantnum = 0

s = 0

num = 0

while num != 999:
    if quantnum == 0:
        num = int(input('Digite um número: '))
    else:
        num = int(input('Digite outro número: '))

    if num != 999:
        quantnum += 1
        s += num

print('Foram digitados {} números no total.'.format(quantnum))

print('A soma entre eles foi de {}.'.format(s))