forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m'
}

print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)
print(f'{forms["bold"]}CONDIÇÃO ALUNO{forms["limpa"]}'.center(60))
print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)

cond = {}

cond['nome'] = str(input('>>> Digite o nome do aluno: ')).strip()
cond['media'] = float(input(f'>>> Média de {cond["nome"]}: '))

if cond['media'] < 5:
    cond['situação'] = '\033[31mReprovado\033[m'

elif cond['media'] < 7:
    cond['situação'] = '\033[33mRecuperação\033[m'

else:
    cond['situação'] = '\033[32mAprovado\033[m'
    
print('-' * 60)
for k, v in cond.items():
    print(f'... {k} é igual a {v}.')