from datetime import date

for c in range(1, 8):
    anonasc = int(input('Digite o ano de nascimento: '))

    idade = date.today().year - anonasc

    if idade >= 18:
        print('Está na MAIORIDADE')
    else:
        print('NÃO está na MAIORIDADE')