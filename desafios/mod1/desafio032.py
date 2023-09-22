from datetime import date

ano = int(input('Digite o ano a ser analisado ou digite o número 0 para analisar o ano atual: '))

cores = {'limpa': '\033[m',
         'amarelo': '\033[1;33m'}

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('>>> O ano {} é um ano {}BISSEXTO.{}'.format(ano, cores['amarelo'], cores['limpa']))
else:
    print('>>> O ano {} NÃO é {}BISSEXTO.{}'.format(ano, cores['amarelo'], cores['limpa']))