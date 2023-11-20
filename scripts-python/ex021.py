forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m'
}

num = 6

def Titulo(title):
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
    print(f'{forms["bold"]}{title}{forms["limpa"]}'.center(60))
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)

def Fatorial(n):
    for c in range(n - 1, 1, -1):
        n *= c
    return n

# Programa Principal
Titulo('MODULARIZAÇÃO EM PYTHON')
fat = Fatorial(num)
print(f'... O fatorial de {num} é igual a {fat}.')