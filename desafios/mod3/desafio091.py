from random import randint
from time import sleep

forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m'
}

print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)
print(f'{forms["bold"]}JOGAR DADOS{forms["limpa"]}'.center(60))
print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)

jogadas = {}

pos = 1

for c in range(4):
    jogadas[f'Jogada{c + 1}'] = (randint(1, 6))

    if c > 0 and jogadas[f'Jogada{c + 1}'] > jogadas[f'Jogada{c}']:
        print()

print(jogadas)

print('-=' * 30)
print(' Ranking dos jogadores '.center(60, '='))

for k, j in jogadas.items():
    print(f'{pos}° lugar: {k} com {j}.')
    pos += 1
    sleep(1)