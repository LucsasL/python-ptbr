print('=' * 30)
print('{:^30}'.format('SUPER POGRESSÃO ARITMÉTICA'))
print('=' * 30)

primeiro = int(input('>>> Digite o primeiro termo: '))

raz = int(input('>>> Digite a razão: '))

termo = primeiro

cont = 1

while cont <= 10:
    print('{} > '.format(termo), end='')
    termo += raz
    cont += 1

print('FIM')

add = int(input('>>> Quantos termos a mais quer adicionar?: '))

while add == 0:
    print('{} > '.format(termo), end='')
    termo += raz

print('FIM')

print('\n... Finalizando programa...')