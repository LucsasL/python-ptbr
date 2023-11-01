# Solução sem parênteses
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

listaParent = []

for car in expr:
    if car == '(':
        listaParent.append('(')

    elif car == ')':
        if len(listaParent) > 0:
            listaParent.pop()

        else:
            listaParent.append(')')
            break

if len(listaParent) == 0:
    print(f'Sua expressão {forms["verde"]}ESTÁ VALIDA.{forms["limpa"]}')

else:
    print(f'Sua expressão {forms["vermelho"]}NÃO ESTÁ VALIDA.{forms["limpa"]}')