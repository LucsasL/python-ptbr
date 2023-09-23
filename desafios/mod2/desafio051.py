print('=' * 23)
print('{:^}'.format('10 PRIMEIROS TERMOS PA'))
print('=' * 23)

term = int(input('Digite o primeiro termo: '))

raz = int(input('Digite a razão: '))

PA = 0

print(term, end=' > ')

for c in range(0, 9):
    PA = PA + raz
    print(PA, end=' > ')

print('FIM')