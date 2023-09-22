num = int(input('Me diga um número qualquer: '))

cores = {'amarelo': '\033[33m',
         'limpa': '\033[m'}

if num % 2 == 0:
    print('O número {} é {}PAR.{}'.format(num, cores['amarelo'], cores['limpa']))
else:
    print('O número {} é {}ÍMPAR.{}'.format(num, cores['amarelo'], cores['limpa']))