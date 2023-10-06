from time import sleep

forms = {
    'limpa': '\033[m',
    'bold': '\033[1;37m',
    'padrao': '\033[37m',
    'roxo': '\033[1;35m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'azul': '\033[34m'
}

Times = ('Botafogo', 'Bragantino', 'Grêmio', 'Palmeiras', 'Flamengo', 'Fluminense', 'Atlético-MG', 'Athletico-PR', 'Fortaleza', 'São Paulo', 'Cuiabá',  'Cruzeiro', 'Corinthians', 'Internacional', 'Santos', 'Goiás', 'Vasco da Gama', 'Bahia', 'América-MG', 'Coritiba')

print('{}={}'.format(forms['roxo'], forms['limpa']) * 160)
print(f'{forms["bold"]}{"Campeonato Brasileiro de Futebol":^160}{forms["limpa"]}')
print('{}={}'.format(forms['roxo'], forms['limpa']) * 160)

while True:
    print(f'\n{forms["bold"]}{forms["azul"]}[1]{forms["bold"]} Mostrar times do Brasileirão Séria A em ordem alfabética{forms["limpa"]}')
    print(f'{forms["bold"]}{forms["azul"]}[2]{forms["bold"]} Mostrar os cincos melhores times do Brasileirão Série A{forms["limpa"]}')
    print(f'{forms["bold"]}{forms["azul"]}[3]{forms["bold"]} Mostrar os quatro piores times do Brasileirão Série A{forms["limpa"]}')
    print(f'{forms["bold"]}{forms["azul"]}[4]{forms["bold"]} Mostrar posição da Chapecoense{forms["limpa"]}')
    print(f'{forms["bold"]}{forms["azul"]}[5]{forms["bold"]} Sair{forms["limpa"]}')

    Esc = int(input(f'\n{forms["padrao"]}>>> Escolha a demonstração da lista [1 a 5]: '))
    print(f'{forms["bold"]}-{forms["limpa"]}' * 50)

    if Esc == 1:
        print(f'{forms["bold"]}... Times em ordem alfabética: ')
        print(f'... {sorted(Times)}')
        print(f'{forms["bold"]}-{forms["limpa"]}' * 50)
        sleep(4)

    elif Esc == 2:
        print(f'{forms["bold"]}... Os cinco primeiros colocados em ordem foram: ')
        print(f'... {forms["verde"]}{Times[:5]}{forms["limpa"]}')
        print(f'{forms["bold"]}-{forms["limpa"]}' * 50)
        sleep(4)

    elif Esc == 3:
        print(f'{forms["bold"]}... Os quatro últimos colocados em ordem foram: ')
        print(f'... {forms["vermelho"]}{Times[-4:]}{forms["limpa"]}')
        print(f'{forms["bold"]}-{forms["limpa"]}' * 50)
        sleep(4)

    elif Esc == 4:
        print(f'{forms["bold"]}... A Chapecoense está na posição .')
        print(f'... {Times}')
        print(f'{forms["bold"]}-{forms["limpa"]}' * 50)
        sleep(4)

    elif Esc == 5:
        break

    else:
        while True:
            Esc = int(input(f'\n{forms["padrao"]}>>> Escolha inválida! Digite novamente [1 a 5]: '))
            print(f'{forms["bold"]}-{forms["limpa"]}' * 50)

            if Esc == 1:
                print(f'{forms["bold"]}... Times em ordem alfabética: ')
                print(f'... {sorted(Times)}')
                print(f'{forms["bold"]}-{forms["limpa"]}' * 50)
                sleep(4)
                break

            elif Esc == 2:
                print(f'{forms["bold"]}... Os cinco primeiros colocados em ordem foram: ')
                print(f'... {forms["verde"]}{Times[:5]}{forms["limpa"]}')
                print(f'{forms["bold"]}-{forms["limpa"]}' * 50)
                sleep(4)
                break

            elif Esc == 3:
                print(f'{forms["bold"]}... Os quatro últimos colocados em ordem foram: ')
                print(f'... {forms["vermelho"]}{Times[-4:]}{forms["limpa"]}')
                print(f'{forms["bold"]}-{forms["limpa"]}' * 50)
                sleep(4)
                break

            elif Esc == 4:
                print(f'{forms["bold"]}... A Chapecoense está na posição .')
                print(f'... {Times}')
                print(f'{forms["bold"]}-{forms["limpa"]}' * 50)
                sleep(4)
                break

            elif Esc == 5:
                break

    if Esc == 5:
            break