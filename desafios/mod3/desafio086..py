forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m'
}

print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)
print(f'{forms["bold"]}Matrizes em Python{forms["limpa"]}'.center(60))
print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)

matriz = [[], [], []]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(str(input(f'>>> Digite um valora para a posição [{l}, {c}]: ')).strip())

print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]:^5} ]', end='' if c < 2 else '\n')