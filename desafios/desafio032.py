ano = int(input('Digite o ano atual: '))

anobi = ano % 4

if anobi == 0:
    print('>>> O ano {} é um ano bissexto.'.format(ano))
else:
    print('>>> O ano {} não é um ano bissexto.'.format(ano))