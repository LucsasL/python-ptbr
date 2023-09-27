quant = int(input('>>> Digite um número: '))

aux = 0

fib = 0

n1 = 1

n2 = 0

rep = 1

while rep != quant:
    print(fib, ' > ', end='')
    fib = n1 + n2
    aux = n1
    n1 = n2
    n2 = aux
    rep += 1

print('... Foram solicitados {} números da sequência de fibonacci.'.format(quant))