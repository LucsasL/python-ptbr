forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m',
}

def Titulo(title):
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
    print(f'{forms["bold"]}{title}{forms["limpa"]}'.center(60))
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)

def Fatorial(num, show = False):
    '''
    -> Calcula o fatorial de um número.
    :param num: Número a ser calculado.
    :param show: (opcional) Mostra operação de caculo.
    :return: O valor do fatorial do número "num".
    '''
    count = num
    if show == True:
        for c in range(num, 0, -1):
            print(f'{c} x ' if c > 1 else f'{c} = ', end='')

    for c in range(count - 1, 1, -1):
        num *= c

    return num

# Programa Principal7
Titulo('CALCULANDO FATORIAL ATRAVÉS DE FUNÇÕES')
print(Fatorial(5, True))
help(Fatorial)