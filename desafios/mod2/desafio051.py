print('=' * 23)
print('{:^}'.format('10 PRIMEIROS TERMOS PA'))
print('=' * 23)

term = int(input('Digite o primeiro termo: '))

raz = int(input('Digite a razão: '))

décimo = term + (10 - 1) * raz

for c in range(term, décimo + raz, raz):
    print(c, end=' > ')

print('FIM')