print('=' * 30)
print('{:^30}'.format('SUPER POGRESSÃO ARITMÉTICA'))
print('=' * 30)

primeiro = int(input('Digite o primeiro termo: '))

raz = int(input('Digite a razão: '))

termo = primeiro

cont = 1

total = 0

add = 10

while add != 0:
    total += add
    
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo += raz
        cont += 1

    print('PAUSA')

    add = int(input('Quantos termos você quer mostrar a mais?: '))

print('\n... Foram mostrados {} termos no total.'.format(cont))

print('\n... Finalizando programa...')