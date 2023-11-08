from random import randint

forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m'
}

print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)
print(f'{forms["bold"]}CONDIÇÃO ALUNO{forms["limpa"]}'.center(60))
print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)

jogadas = {
    'Jogada1': '',
    'Jogada2': '',
    'Jogada3': '',
    'Jogada4': ''
}

pos = 1

for c in range(4):
    jogadas[f'Jogada{c + 1}'] = (randint(1, 6))

print(jogadas)

print('-=' * 30)
print('Ranking dos jogadores:')

for k, j in jogadas.items():
    print(f'{c}° lugar: {k} com {j}')
    pos += 1