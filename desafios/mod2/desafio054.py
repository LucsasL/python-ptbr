from datetime import date

contmai = 0

for c in range(1, 8):
    anonasc = int(input('>>> Digite o ano de nascimento: '))

    idade = date.today().year - anonasc

    if idade >= 18:
        print('... Está na MAIORIDADE')
        contmai += 1
    else:
        print('... NÃO está na MAIORIDADE')

if contmai == c and:
    print('... Todas as pessoas listadas estão na maioridade.')
elif contmai > 0 and contmai < c:
    print('... Das pessoas digitadas, apenas {} está(ão) na maioridade'.format(contmai))
else:
    print('... Ninguém listado está na maioridade.')

# Em desenvolvimento