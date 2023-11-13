from random import randint
from time import sleep
from operator import itemgetter

forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m'
}

print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)
print(f'{forms["bold"]}JOGAR DADOS{forms["limpa"]}'.center(60))
print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)

jogadas = {
    'Jogador 1': randint(1, 6),
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6)
}

ranking = []

for i, k in jogadas.items():
    print(f'{i} tirou {k} no dado.')
    sleep(1)

print(' Ranking dos jogadores '.center(60, '='))

ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)

for i, k in enumerate(ranking):
    print(f'{i + 1}° lugar: {k[0]} com {k[1]}.')
    sleep(1)