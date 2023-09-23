s = 0

cont = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        s = s + c
        print(c, end=', ')

print('\n... O resultado da soma dos {} números ímpares é igual a: {}.'.format(cont, s))