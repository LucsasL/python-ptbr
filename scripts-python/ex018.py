pessoas = {
    'Nome': 'Gustavo',
    'Sexo': 'Masculino',
    'Idade': 22
}

print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos e é do sexo {pessoas["Sexo"]}.')

pessoas['Peso'] = 98.5

for k, v in pessoas.items():
    print(f'{k} = {v}')

Brasil = []

Estado = {
    'UF': 'Rio de Janeiro',
    'Sigla': 'RJ'
}

Estado2 = {
    'UF': 'São Paulo',
    'Sigla': 'SP'
}

Brasil.append(Estado)
Brasil.append(Estado2)

print('-' * 60)
print(Brasil)

Estado3 = dict()

print('-' * 60)
for c in range(3):
    Estado3['UF'] = str(input('>>> Digite uma Unidade Federativa: ')).strip().capitalize()
    Estado3['Sigla'] = str(input('>>> Digite a sigla: ')).strip().upper()
    Brasil.append(Estado3.copy())
    
print('-' * 60)
for e in Brasil:
    for k, v in e.items():
        print(f'... O campo {k} tem valor {v}.')
        print('-' * 60)