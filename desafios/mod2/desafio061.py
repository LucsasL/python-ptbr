print('=' * 30)
print('{:^30}'.format('10 PRIMEIROS TERMOS PA'))
print('=' * 30)

primeiro = int(input('Digite o primeiro termo: '))

raz = int(input('Digite a razão: '))

termo = primeiro

cont = 1

while cont <= 10:
    print('{} > '.format(termo), end='')
    termo += raz
    cont += 1

print('FIM')