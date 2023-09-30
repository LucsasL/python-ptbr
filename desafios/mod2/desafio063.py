print('-=-' * 10)
print('{:^30}'.format('SEQUÊNCIA DE FIBONACCI'))
print('-=-' * 10)
quant = int(input('>>> Digite a quantidade de termos a ser mostrado: '))

fib = 0

n1 = 0

n2 = 1

rep = 2

print('{}  >  {}  >  '.format(n1, n2), end='')

while rep != quant:
    fib = n1 + n2
    print(fib, ' > ', end='')
    n1 = n2
    n2 = fib
    rep += 1

print('FIM')

print('\n... Foram solicitados {} números da sequência de fibonacci.'.format(quant))