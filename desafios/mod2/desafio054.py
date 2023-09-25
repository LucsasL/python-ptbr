from datetime import date

contmai = 0

contmen = 0

for c in range(1, 8):
    anonasc = int(input('>>> Digite o ano de nascimento: '))

    idade = date.today().year - anonasc

    if idade >= 18:
        contmai += 1
    else:
        contmen += 1

if contmai == c:
    print('... Todas as pessoas listadas estão na maioridade.')

elif contmai == 1 and contmen < c:
    print('... Das pessoas digitadas, apenas {} está na maioridade e {} não estão na maioridade.'.format(contmai, contmen))

elif contmai < c and contmen == 1:
    print('... Das pessoas digitadas, apenas {} estão na maioridade e {} não está na maioridade.'.format(contmai, contmen))

else:
    print('... Ninguém listado está na maioridade.')