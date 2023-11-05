from random import randint
from time import sleep

forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m',
    'verde': '\033[1;32m'
}

print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)
print(f'{forms["bold"]}JOGAR NA MEGA SENA{forms["limpa"]}'.center(60))
print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)

jogosMegaSena = []
RandNum = []
count = 0

jogos = int(input('>>> Quantos jogos serão jogados?: '))

print(f' SORTEANDO {jogos} JOGOS '.center(60, '='))

for j in range(0, jogos):
    while count < 6:
        RandNum.append(randint(0, 60))

        if count > 0 and RandNum[count] in RandNum[:count]:
            RandNum.pop()
            count -= 1
        
        count += 1
    count = 0

    RandNum.sort()
    jogosMegaSena.append(RandNum[:])
    RandNum.clear()

for j in range(0, jogos):
    print(f'... Jogo {j + 1}: {jogosMegaSena[j]}')
    sleep(1)

print(f'{forms["verde"]} < BOA SORTE! > {forms["limpa"]}'.center(70, '='))