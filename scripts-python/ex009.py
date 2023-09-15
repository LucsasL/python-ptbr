nome = str(input('Qual é seu nome?: ')).capitalize().strip()

if nome == 'Gustavo':
    print('Que nome lindo você tem.')
else:
    print('Seu nome é  tão normal.')

print('Bom dia {}.'.format(nome))

# ---------------------------------------------------------------------

n1 = float(input('Digite a primeira nota: '))

n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2) / 2

print('A sua média é de {:.1f}.'.format(m))

if m >= 5:
    print('Parabéns, sua média foi boa.')
else:
    print('Sua média não foi boa o suficiente. ESTUDE MAIS!')