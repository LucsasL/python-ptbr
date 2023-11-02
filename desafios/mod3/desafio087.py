forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m'
}

print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)
print(f'{forms["bold"]}Matrizes em Python{forms["limpa"]}'.center(60))
print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)

matrix = []
soma = somaTer = maiorSeg = 0

for l in range(0, 3):
    lin = []

    for c in range(0, 3):
        lin.append(str(input(f'>>> Digite um valora para a posição [{l}, {c}]: ')).strip())
    matrix.append(lin[:])

print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)

for c in range(0, 3):
    print(f' {matrix[c]} ')

for l in matrix:
    soma += matrix[l]

for c in matrix:
    # Em desenvolvimento
    print('')

print(f'... A soma de todos os valores foi igual a {soma}.')
print(f'... A soma dos valores da terceira coluna é igual a {somaTer}.')
print(f'... O maior número da segunda linha {maiorSeg}.')