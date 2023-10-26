numeros = []

par = []

impar = []

while True:
    num = int(input('>>> Digite um número: '))
    numeros.append(num)

    if num % 2 == 0:
        par.append(num)

    else:
        impar.append(num)

    resp = str(input('>>> Adicionar mais um número? [S / N]: ')).strip().upper()[0]

    if resp != 'S' and resp != 'N':
        while True:
            resp = str(input('>>> Valor inválido! Digite novamente [S / N]: ')).strip().upper()[0]

            if resp == 'S' or resp == 'N':
                break
        
        if resp == 'N':
            break

    elif resp == 'N':
        break

print(f'\n... Você digitou os valores: {numeros}')
print('-=-' * 40)
print(f'... Os valores ímpares foram: {impar}')
print(f'... Os valores pares foram: {par}')