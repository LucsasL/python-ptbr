forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m'
}

def Title(title):
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
    print(f'{title}'.center(60))
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)

Title("Muito foda essas funções")