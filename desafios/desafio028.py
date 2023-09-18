from random import randint
from time import sleep

num = randint(0, 5) # faz o computador pensar

cores = {'limpa': '\033[m',
         'bold': '\033[1m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m'}

print('\033[1;35m-=-\033[m' * 20)
print('{}Vou pensar em um número entre 0 e 5. Tente adivinhar...'.format(cores['bold']))
print('\033[1;35m-=-\033[m' * 20)

answer = int(input('Em que número eu pensei?: ')) # Jogador tenta adivinhar

print('PROCESSANDO...')
sleep(1.5)

if answer == num:
    print('>>> {}PARABÉNS!{} Você conseguiu me vencer!'.format(cores['verde'], cores['limpa']))
else:
    print('{}GANHEI.{} Eu pensei no número {} e não no {}.'.format(cores['vermelho'], cores['limpa'],num, answer))