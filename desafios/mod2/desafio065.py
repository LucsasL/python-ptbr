fim = False

quantnum = m = maior = 0

menor = 999999999999999999999

while fim != True:
    if quantnum == 0:
        num = int(input('>>> Digite um número: '))
    else:
        num = int(input('>>> Digite outro número: '))

    resp = str(input('>>> Quer continuar a adicionar números? [S / N]: ')).upper().strip()

    quantnum += 1

    m += num

    if num > maior:
        maior = num

    if num < menor:
        menor = num

    if resp == 'N':
        fim = True
    elif resp == 'S':
        num = int(input('>>> Digite outro número: '))
    else:
        while resp != 'S' or 'N':
            resp = str(input('>>> O valor digitado é invalido! Tente novamente [S / N]: ')).upper().strip()

            if resp == 'N':
                fim = True

m = m / quantnum

print('... A média dos números digitados é {:.2f}.'.format(m))