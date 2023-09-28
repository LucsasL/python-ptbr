print('=' * 30)
print('{:^30}'.format('10 PRIMEIROS TERMOS PA'))
print('=' * 30)

fim = False

adicao = 0

while fim == False:
    if adicao == 0:
        primeiro = int(input('>>> Digite o primeiro termo: '))

    raz = int(input('>>> Digite a razão: '))

    termo = primeiro

    cont = 1

    if adicao == 0:
        while cont <= 10:
            print('{} > '.format(termo), end='')
            termo += raz
            cont += 1
        
        PA = termo

    else:
        while cont <= 10:
            print('{} > '.format(PA), end='')
            PA += raz
            cont += 1
        
        PA = PA

    print('FIM')

    resp = str(input('\n>>> Quer continuar a somar números na PA? [S / N]:')).upper()[0].strip()

    if resp == 'S':
        fim = False
        adicao += 1
    elif resp == 'N':
        fim = True
    else:
        while resp not in 'SN':
            resp = str(input('\n>>> Opção inválida! Tente novamnente [S / N]: ')).upper()[0].strip()

        if resp == 'N':
            fim = True
        elif resp == 'S':
            adicao += 1

print('\n... adições extras: {}.'.format(adicao))
print('\n... Finalizando programa...')