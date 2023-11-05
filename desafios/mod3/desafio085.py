forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m'
}

print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)
print(f'{forms["bold"]}Lista pares e ímpares{forms["limpa"]}'.center(60))
print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)

lista = [[], []]
valor = 0

for c in range(0, 7):
    valor = int(input(f'>>> Digite o {c + 1}° número: '))

    if valor % 2 == 0:
        lista[0].append(valor)

    else:
        lista[1].append(valor)

lista[0].sort()
lista[1].sort()

print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
print(f'... Os números pares digitados foram: {lista[0]}')
print(f'... OS números ímpares digitados foram: {lista[1]}')