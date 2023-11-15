from time import sleep

forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m',
}

resp = ''

def Titulo(title):
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
    print(f'{forms["bold"]}{title}{forms["limpa"]}'.center(60))
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)

def Contador(ini, fim, passo):
    if fim > ini:
        print(f'... Contando de {ini} a {fim} de {passo} em {passo}:')
        for c in range(ini, fim + 1, passo):
            print(f'{c} ', end='')
            sleep(.5)
    else:
        print(f'... Contando de {ini} a {fim} de {passo} em {passo}:')
        for c in range(ini, fim, passo):
            print(f'{c} ', end='')
            sleep(.5)
    print('FIM!\n')

# Programa Principal
Titulo('CONTADOR')
Contador(1, 10, 1)
Contador(10, 0, -2)

while resp != 'N':
    resp = str(input('>>> Criar contagem personzalizada? [S / N]: ')).strip().upper()[0]

    if resp == 'S':
        Contador(int(input('>>> Digite o Inicio: ')), int(input('>>> Digite o fim da contagem: ')), int(input('>>> Digite o passo [+ / -]: ')))

    if resp != 'S' and resp != 'N':
        while True:
            resp = str(input('>>> Opção inválida! Digite novamente [S / N]: ')).strip().upper()[0]

            if resp == 'S':
                Contador(int(input('>>> Digite o Inicio: ')), int(input('>>> Digite o fim da contagem: ')), int(input('>>> Digite o passo [+ / -]: ')))
                break

            elif resp == 'N':
                break