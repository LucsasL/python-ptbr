numeros = []

while True:
    num = float(input('>>> Digite um número: '))
    numeros.append(num)

    resp = str(input('>>> Quer adicionar mais números? [S / N]: ')).strip().upper()[0]

    if resp != 'S' and resp != 'N':
        while True:
            resp = str(input('>>> Valor inválido! Digite novamente [S / N]: ')).strip().upper()[0]

            if resp == 'S' or resp == 'N':
                break
        
        if resp == 'N':
            break

    elif resp == 'N':
        break

print(f'... No total, foram digitados {len(numeros)} números.')
print(f'... A lista de números ordenadas é: {numeros.sort(reverse=True)}') # A propriedaded reverse não funcionou ainda

if 5 in numeros:
    print(f'... o valor 5 está na lista.')

else:
    print('... O número 5 não está na lista.')