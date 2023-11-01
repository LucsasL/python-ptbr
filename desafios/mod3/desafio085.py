forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m'
}

print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)
print(f'{forms["bold"]}Lista pares e ímpares{forms["limpa"]}'.center(60))
print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)

lista = []
pares = []
impares = []

for c in range(0, 7):
    num = int(input(f'>>> Digite o {c + 1}° número: '))

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

lista.append(pares)
lista.append(impares)
pares.sort()
impares.sort()

print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
print(f'... Os números pares digitados foram: {pares}')
print(f'... OS números ímpares digitados foram: {impares}')