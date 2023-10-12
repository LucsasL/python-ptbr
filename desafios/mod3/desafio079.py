forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m',
}

print(f'{forms["roxo"]}-{forms["limpa"]}' * 50)
print(f'{forms["bold"]}TESTE DE DESAFIO{forms["limpa"]}'.center(55))
print(f'{forms["roxo"]}-{forms["limpa"]}' * 50)