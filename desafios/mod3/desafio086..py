forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m'
}

print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)
print(f'{forms["bold"]}Matrizes em Python{forms["limpa"]}'.center(60))
print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)

matrix = []
count = 0

for c in range(0, 3):
    lin = []

    for l in range(0, 3):
        lin.append(str(input(f'>>> Digite um valora para a posição {count + 1}: ')).strip())
        count += 1
    matrix.append(lin[:])

for c in range(0, 3):
    print(matrix[c])