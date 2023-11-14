forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m'
}

def Titulo(title):
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
    print(f'{title}'.center(60))
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)

def Soma(n1=0, n2=0):
    print(f'... A = {n1}, B = {n2}')
    s = n1 + n2
    print(f'... A soma entre {n1} e {n2} é igual a {s}')

# Programa principal
Titulo('Muito foda essas funções')
Titulo('Ensinado em um curso')
Titulo('Exercício curso em vídeo')

Soma(4, 5)
Soma(8, 9)
Soma(1, 2)