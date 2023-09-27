num = int(input('Digite um número: '))

proc = num - 1

resp = 'S'

fat = num

while proc != 1:
    fat = fat * proc
    proc -= 1

print('O fatorial de {} é igual a {}.'.format(num, fat))