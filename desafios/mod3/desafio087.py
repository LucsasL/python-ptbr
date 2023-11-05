forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m'
}

print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)
print(f'{forms["bold"]}Matrizes em Python{forms["limpa"]}'.center(60))
print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)

matriz = [[], [], []]
somaPar = somaTer = maiorSeg = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'>>> Digite um valora para a posição [{l}, {c}]: ')))

print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]:^5} ]', end='' if c < 2 else '\n')

        if matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]
    somaTer += matriz[l][2]

for c in range(3):
    if matriz[1][c] > maiorSeg:
        maiorSeg = matriz[1][c]

print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
print(f'... A soma de todos os valores pares foi igual a {somaPar}.')
print(f'... A soma dos valores da terceira coluna é igual a {somaTer}.')
print(f'... O maior número da segunda linha {maiorSeg}.')