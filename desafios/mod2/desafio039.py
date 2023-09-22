from datetime import date

anonasc = int(input('Digite o ano de nascimento: '))

idade = date.today().year - anonasc

if idade > 18:
    tempo = idade - 18
    print('Já se passaram {} anos desde que você devia se alistar no exército, que foi {}.'.format(tempo, (anonasc + 18)))
elif idade == 18:
    print('Já é hora de se alistar no exército.')
else:
    tempo = 18 - idade
    print('Ainda há de se esperar {} anos para se alistar no exército, que será em {}.'.format(tempo, (anonasc + 18)))