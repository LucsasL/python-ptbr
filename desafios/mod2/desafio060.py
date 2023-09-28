num = int(input('Digite um número para calcular seu fatorial: '))

proc = num - 1

resp = 'S'

fat = num

print('Calculando ', num, '! = ', num, end=' x ')

while proc != 1:
    fat = fat * proc
    print(proc, ' x ', end='')
    proc -= 1

print('1 = ', fat)

print('...  O fatorial de {} é igual a {}.'.format(num, fat))