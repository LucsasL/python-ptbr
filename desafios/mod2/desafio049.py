n = int(input('Digite um número: '))

print('-' * 12)
for c in range(1, 11):
    print('{} * {:2} = {}'.format(n, c, (n*c)))
print('-' * 12)