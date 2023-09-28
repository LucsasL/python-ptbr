num = int(input('Digite um número para calcular seu fatorial: '))

proc = num - 1

fat = num

print('Calculando ', num, '! = ', num, end=' x ')

while proc > 0:
    fat *= proc
    print(proc, ' x ' if proc > 1 else ' = {}'.format(fat), end='')
    proc -= 1

print('\n...  O fatorial de {} é igual a {}.'.format(num, fat))