from datetime import date

forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m'
}

print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)
print(f'{forms["bold"]}CONDIÇÃO ALUNO{forms["limpa"]}'.center(60))
print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)

dicio = []
anoAtual = date()

dicio['Nome'] = str(input('>>> Digite o nome: ')).strip().title()
dicio['AnoNasc'] = int(input(f'>>> Digite o ano de nascimento de {dicio["Nome"]}: '))

idade =  anoAtual - dicio['AnoNasc']
dicio['CarteiraTrab'] = idade

print(dicio['CarteiraTrab'])