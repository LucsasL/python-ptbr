forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m',
}

numeros = list()

c = 0

print(f'{forms["roxo"]}-{forms["limpa"]}' * 50)
print(f'{forms["bold"]}DESAFIO CONTADOR DE LISTA{forms["limpa"]}'.center(55))
print(f'{forms["roxo"]}-{forms["limpa"]}' * 50)

while True:
    n = int(input(f'>>> Digite o {c + 1}° número: '))
    numeros.append(n)

    if c > 0 and n in numeros[:c]:
        print(f'... Número repetido! Não vou adicionar...')
        numeros.pop()
        resp = str(input('>>> Adicionar mais um número? [S / N]:')).strip().upper()

    else:
        resp = str(input('>>> Adicionar mais um número? [S / N]:')).strip().upper()[0]
        c += 1

    if resp != 'S' and resp != 'N':
        while True:
            resp = str(input('>>> Valor inválido! Adicionar mais um número? [S / N]:')).strip().upper()

            if resp == 'N' or resp == 'S':
                break

        if resp == 'N':
            break

    elif resp == 'N':
        break

print('-=' * 20)
print(f'Você digitou os números: {sorted(numeros)}')