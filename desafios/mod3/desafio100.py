from random import randint
from time import sleep

forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m',
}

numeros = []
pares = []

def Titulo(title):
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
    print(f'{forms["bold"]}{title}{forms["limpa"]}'.center(60))
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)

def Sorteia():
    print(f'... Sorteando 5 valores: ', end='')
    for c in range(5):
        numeros.append(randint(0, 50))
        print(f'{numeros[c]}, ' if c < 4 else f'{numeros[c]}.', end='' if c < 4 else '\n')
        sleep(1)
        
def SomaPar(num):
    soma = 0
    for v in num:
        if v % 2 == 0:
            pares.append(v)
            soma += v
    print(f'... Somando todos os valores pares: {pares}, temos {soma}.')

# Programa Principal
Titulo('Calculando números pares com funções')
Sorteia()
SomaPar(numeros)