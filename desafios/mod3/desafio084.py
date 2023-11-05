forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m'
}

print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)
print(f'{forms["bold"]}Analise de pessoas{forms["limpa"]}'.center(60))
print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)

pessoas = []
cadastro = []
c = 0

while True:
    pessoas.append(str(input('>>> Digite o primeiro nome: ')))
    pessoas.append(float(input('>>> Digite a peso [Kg]: ')))
    cadastro.append(pessoas[:])
    pessoas.clear()

    resp = str(input('>>> Adicionar mais uma pessoa? [S / N]: ')).strip().upper()[0]

    if resp != 'S' and resp != 'N':
        while True:
            resp = str(input('>>> Opção inválida! Digite novamente [S / N]: ')).strip().upper()[0]

            if resp == 'S' or resp == 'N':
                break

        if resp == 'N':
            break

    elif resp == 'N':
        break

for p in cadastro:
    if c == 0:
        maisPes = menPes = p[1]
    
    if p[1] > maisPes:
        maisPes = p[1]
    
    if p[1] < menPes:
        menPes = p[1]
    c += 1

print(f'\n... Foram cadastradas {len(cadastro)} pessoas.')
print(f'... O maior peso foi {maisPes:.2f}Kg e eram de: ', end='')

for p in cadastro:
    if p[1] == maisPes:
        print(f'[{p[0]}] ', end='')
    
print(f'\n... O menor peso foi {menPes:.2f}Kg e eram de: ', end='')

for p in cadastro:
    if p[1] == menPes:
        print(f'[{p[0]}] ', end='' if p[1] == menPes else '\n')