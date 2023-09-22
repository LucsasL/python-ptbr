s = 0

for c in range(0, 500):
    if c % 2 == 1 and c // 3 == 0:
        s = s + c
        print(c)

print('O resultado das somas é igual a: {}.'.format(s))