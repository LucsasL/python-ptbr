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

dicio = {}
anoAtual = date.today().year

dicio['Nome'] = str(input('>>> Digite o nome: ')).strip().title()
dicio['AnoNasc'] = int(input(f'>>> Digite o ano de nascimento de {dicio["Nome"]}: '))

idade = anoAtual - dicio['AnoNasc']
dicio['CarteiraTrab'] = int(input(f'>>> Número da carteira de trabalho {forms["vermelho"]}(0 pra quem não tem: ){forms["limpa"]}: '))

if dicio['CarteiraTrab'] == 0:
    SemCarteira = 'Não tem carteira'

print(idade)

print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)