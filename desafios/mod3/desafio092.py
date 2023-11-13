from datetime import date

forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m',
    'vermelho': '\033[1;31m'
}

print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)
print(f'{forms["bold"]}ANALISE APOSENTADORIA{forms["limpa"]}'.center(60))
print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)

dados = dict()
anoAtual = date.today().year

dados['Nome'] = str(input('>>> Digite o nome: ')).strip().title()
AnoNasc = int(input(f'>>> Digite o ano de nascimento de {dados["Nome"]}: '))
dados['Idade'] = anoAtual - AnoNasc
dados['CTPS'] = int(input(f'>>> Número da carteira de trabalho {forms["vermelho"]}(0 pra quem não tem: ){forms["limpa"]}: '))

if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('>>> Ano de contratação: '))
    dados['Salário'] = float(input('>>> Qual o salário?: R$'))
    dados['Aposentadoria'] = dados['Idade'] + (dados['Contratação'] + 35 - anoAtual)

print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
for i, v in dados.items():
    print(f'    - {i} tem o valor {v}')