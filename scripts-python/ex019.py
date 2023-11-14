forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m'
}

def Titulo(title):
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
    print(f'{title}'.center(60))
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)

def Soma(*num):
    s = 0
    for v in num:
        s += v
    print(s)

def Dobra(lst):
    for i in range(len(lst)):
        lst[i] *= 2

# Programa principal
Titulo('Muito foda essas funções')
Titulo('Ensinado em um curso')
Titulo('Exercício curso em vídeo')

Soma(4, 5, 2, 3, 7)
Soma(8, 9, 5)
Soma(1, 2, 8, 4)

Valores = [5, 9, 4, 2, 3]

Dobra(Valores)

print(Valores)