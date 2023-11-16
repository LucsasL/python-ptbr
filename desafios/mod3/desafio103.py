forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m'
}

def Titulo(title):
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
    print(f'{forms["bold"]}{title}{forms["limpa"]}'.center(60))
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)

def Ficha(nome='', gols=0):
    if nome == '':
        nome = '<desconhecido>'

    if gols == '':
        gols = 0

    print(f'{forms["roxo"]}-={forms["limpa"]}' * 25)
    print(f'{forms["bold"]}{"Nome":40}{"Gols":>10}{forms["limpa"]}')
    print(f'{forms["roxo"]}-{forms["limpa"]}' * 50)
    print(f'{nome:40}{gols:>10}')
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 25)

# Programa Principal
Titulo('FICHA DE GOLS')
Ficha(str(input('>>> Digite o nome do jogador: ')).strip().title(), str(input('>>> Digite a quantidade de gols: ')))