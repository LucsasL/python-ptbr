forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m',
    'verde': '\033[32m',
    'vermelho': '\033[31m'
}

print(f'{forms["roxo"]}={forms["limpa"]}' * 70)
print(f'{forms["bold"]}ANALISADOR DE EXPRESSÕES NÚMERICAS{forms["limpa"]}'.center(70))
print(f'{forms["roxo"]}={forms["limpa"]}' * 70)

expr = str(input('>>> Digite uma expressão numérica: ')).strip()

if expr.count('(') == expr.count(')'):
    print(f'... Sua expressão é {forms["verde"]}valida.{forms["limpa"]}')

else:
    print(f'... Sua expressão é {forms["vermelho"]}inválida.{forms["limpa"]}')