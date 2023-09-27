fim = False

quantnum = m = maior = 0

error = 'ERROR'

menor = 999999999999999999999

while fim != True:
    # Diferentes formas de pedir um número
    if quantnum == 0:
        num = int(input('>>> Digite um número: '))
    else:
        num = int(input('>>> Digite outro número: '))

    quantnum += 1

    m += num

    # Verificação de números maiores e menores
    if num > maior:
        maior = num

    if num < menor:
        menor = num

    resp = str(input('>>> Quer continuar a adicionar números? [S / N]: ')).upper().strip()

    # Analise da resposta sobre adição de mais números
    if resp == 'N':
        fim = True

    elif resp == 'S':
        fim = False

    else:
        while resp not in 'SN':
            resp = str(input('>>> O valor digitado é inválido! Tente novamente [S / N]: ')).upper().strip()

        if resp == 'N':
            fim = True

m = m / quantnum

print('... A média dos números digitados é {:.2f}.'.format(m))

print('... O maior número foi o {} e o menor número foi o {}.'.format(maior, menor))