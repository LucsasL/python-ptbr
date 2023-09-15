from random import randint

num = randint(0, 5)

answer = int(input('Adivinhe um número pensado pelo computador: '))

if answer == num:
    print('Parabéns! Você acertou o número.')
else:
    print('Você errou. O computador pensou no número {}.'.format(num))