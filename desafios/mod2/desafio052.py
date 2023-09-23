num = int(input('Digite um número: '))

tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
        
    print(c, end='\033[m ')

print('\n... Existem {} divsíveis para o número {}.'.format(tot, num), end='')

if tot == 2:
    print(' Sendo assim um NÚMERO PRIMO.')
else:
    print(' NÃO é um NÚMERO PRIMO.')