forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m'
}

print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)
print(f'{forms["bold"]}CADASTRO DE PESSOAS{forms["limpa"]}'.center(60))
print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)

cadastros = []
pessoas = {}
media = MaioresMedia = Mulheres = count = 0
resp = ''

while resp != 'N':
    if count > 0:
        print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)

    pessoas['Nome'] = str(input('>>> Digite o nome: ')).strip().title()
    pessoas['Idade'] = int(input(f'>>> Digite a idade do {pessoas["Nome"]}: '))
    pessoas['Sexo'] = str(input(f'>>> Digite o sexo do {pessoas["Nome"]} [M / F]: ')).strip().upper()[0]

    if pessoas['Sexo'] != 'M' and pessoas['Sexo'] != 'F':
        while True:
            pessoas['Sexo'] = str(input('>>> Opção inválida! Digite novamente [M / F]: ')).strip().upper()[0]

            if pessoas['Sexo'] == 'M' or pessoas['Sexo'] == 'F':
                break
    
    elif pessoas['Sexo'] == 'F':
        Mulheres += 1

    cadastros.append(pessoas.copy())
    count += 1

    resp = str(input('>>> Adicionar pessoas ao cadastro [S / N]: ')).strip().upper()[0]

    if resp != 'S' and resp != 'N':
        while True:
            resp = str(input('>>> Opção inválida! Digite novamente [S / N]: ')).strip().upper()[0]

            if resp == 'S' or resp == 'N':
                break

for p in cadastros:
    media += p['Idade']

media /= len(cadastros)

for p in cadastros:
    if p['Idade'] > media:
        MaioresMedia += 1

print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
print(f'{"N.":<5}{"Nome":<30}{"Idade":>10}{"Sexo":>10}')
print(f'{forms["roxo"]}-{forms["limpa"]}' * 60)

for i, p in enumerate(cadastros):
    print(f'{i:<5}{p["Nome"]:<30}{p["Idade"]:>10}{p["Sexo"]:>10}')

print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)

# Número de pessoas cadastradas
if len(cadastros) == 1:
    print('... Apenas 1 pessoa foi cadastrada.')

else:
    print(f'... No total, {len(cadastros)} pessoas foram cadastradas.')

# Média
if len(cadastros) == 1:
    print(f'... A média é a mesma que a idade da única pessoa cadastrada, sendo equivalente a {forms["bold"]}{media}.{forms["limpa"]}')

else:
    print(f'... A média de idade de todas as pessoas cadastradas é igual a {forms["bold"]}{media:.2f}.{forms["limpa"]}')

# Analise de mulheres no cadastro
if Mulheres == 0:
    print('... Não há mulheres cadastradas.')

elif Mulheres == 1:
    print(f'... Foi cadastrado apenas {Mulheres} mulher, ', end='')

else:
    print(f'... Foram cadastradas {Mulheres} mulheres no total, sendo essas: ', end='')

    for i, p in enumerate(cadastros):
        if p['Sexo'] == 'F':
            print(f'{p["Nome"]}, ' if i < len(cadastros) - 2 else f'{p["Nome"]}.', end='' if i < len(cadastros) - 2 else '\n')

# Analise de idades com valor acima da média
if len(cadastros) == 1:
    print(f'... Há apenas uma pessoa cadastrada, então sua idade equivale a média.')

elif len(cadastros) > 1:
    if MaioresMedia > 0:
        print(f'... De todas as pessoas cadastradas, {MaioresMedia} pessoas tem idade maior que a média, sendo essas: ', end='')

        for i, p in enumerate(cadastros):
            if p['Idade'] > media:
                print(f'{p["Nome"]}, ' if i < len(cadastros) - 2 else f'{p["Nome"]}.', end='' if i < len(cadastros) - 2 else '\n')
    
    else:
        print(f'... Não há pessoas com idade acima da média.')