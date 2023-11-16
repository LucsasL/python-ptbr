# Declaração de variáveis
resp = ''

forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'inverso': '\033[1;40m',
    'roxo': '\033[1;35m',
    'vermelho': '\033[31m'
}

# Funções
def Titulo(title):
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
    print(f'{forms["bold"]}{title}{forms["limpa"]}'.center(60))
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)

def Ajuda(doc):
    print(f'{forms["inverso"]}')
    help(doc)
    print(f'{forms["limpa"]}')

# Programa Principal
Titulo('SISTEMA DE AJUDA PyHELP')

while True:
    resp = str(input(f'>>> Função ou Biblioteca {forms["vermelho"]}[FIM para finalizar]{forms["limpa"]}: ')).strip()

    if resp not in 'FIMfimFim':
        Ajuda(resp)
        print(resp)
    
    else:
        break