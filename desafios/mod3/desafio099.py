from time import sleep

forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m',
}

def Titulo(title):
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
    print(f'{forms["bold"]}{title}{forms["limpa"]}'.center(60))
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)

def Maior(*num):
    for i, v in enumerate(num):
        if i == 0:
            Maior = v

        if v > Maior:
            Maior = v

    print(f'{forms["roxo"]}-={forms["limpa"]}' * 60)
    print('... Analisando os valores passados...')
    sleep(1)
    if len(num) > 0:
        if len(num) == 1:
            for v in num:
                print(f'... Foi informado apenas o valor {v}.')
            print(f'... O maior valor informado foi o {Maior}.')

        else:
            print(f'... Foram informados {len(num)} valores ao todo, sendo eles: ', end='')

            for i, v in enumerate(num):
                print(f'{v}, ' if i < len(num) - 1 else f'{v}.', end='' if i < len(num) - 1 else '\n')
                sleep(.8)

            print(f'... O maior valor informado foi o {Maior}.')

    else:
        print(f'... Nenhum valor foi informado.')

# Programa Principal
Maior(2, 9, 4, 5, 7, 1)
Maior(4, 7, 0)
Maior(1, 2)
Maior(8)
Maior()