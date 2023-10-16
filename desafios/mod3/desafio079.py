forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m',
}

numeros = list()

print(f'{forms["roxo"]}-{forms["limpa"]}' * 50)
print(f'{forms["bold"]}TESTE DE DESAFIO{forms["limpa"]}'.center(55))
print(f'{forms["roxo"]}-{forms["limpa"]}' * 50)

for c in range(0, 5):
    numeros.append(int(input(f'>>> Digite o {c + 1} número: ')))

print(numeros)