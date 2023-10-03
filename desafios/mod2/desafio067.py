mult = 1

while True:
    print('-' * 30)
    num = int(input('>>> Digite o número a ser multiplicado [número negativo para parar]: '))
    print('-' * 30)
    if num >= 0:
        while mult <= 10:
            print(f'{num} X {mult:2} = {num * mult}')
            mult += 1
    mult = 1

    if num < 0: 
        break

print('\nFINALIZANDO PROGRAMA...')