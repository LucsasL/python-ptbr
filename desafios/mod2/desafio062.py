print('=' * 30)
print('{:^30}'.format('SUPER POGRESSÃO ARITMÉTICA'))
print('=' * 30)

primeiro = int(input('>>> Digite o primeiro termo: '))

raz = int(input('>>> Digite a razão: '))

termo = primeiro

cont = 1

add = 1

while add != 0:
    if cont == 1:
        while cont <= 10:
            print('{} > '.format(termo), end='')
            termo += raz
            cont += 1
    else:
        add = int(input('>>> Quantos termos a mais quer adicionar?: '))

        while add == cont:
            print('{} > '.format(termo), end='')
            termo += raz
            cont += 1

    print('FIM')

print('\n... Finalizando programa...')