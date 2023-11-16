forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m'
}

def Titulo(title):
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
    print(f'{title}'.center(60))
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)

# Programa Principal
Titulo('2° AULA DE FUNÇÕES')