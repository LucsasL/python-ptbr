from random import randint
from time import sleep

num = randint(0, 5) # faz o computador pensar

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

answer = int(input('Em que número eu pensei?: ')) # Jogador tenta adivinhar

print('PROCESSANDO...')
sleep(1.5)

if answer == num:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI. Eu pensei no número {} e não no {}.'.format(num, answer))