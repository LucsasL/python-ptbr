cores = {'limpa': '\033[m',
         'bold': '\033[1m',
         'verde': '\033[1;32m',
         'vermelho': '\033[1;31m',
         'roxo': '\033[1;35m'}

print('{}-=-{}'.format(cores['roxo'], cores['limpa']) * 20)
print('{}Analisador de triângulos{}'.format(cores['bold'], cores['limpa']))
print('{}-=-{}'.format(cores['roxo'], cores['limpa']) * 20)

L1 = float(input('Digite o tamanho do primeiro lado: '))
L2 = float(input('Digite o tamanho do segundo lado: '))
L3 = float(input('Digite o tamanho do terceiri lado: '))

if L1 < L2 + L3 and L2 < L1 + L3 and L3 < L1 + L2:
    print('>>> Com as medidas apresentadas, {}É POSSÍVEL FORMAR{} um triângulo.'.format(cores['verde'], cores['limpa']))

else:
    print('>>> Com as medidas dispostas, {}NÃO É POSSÍVEL FORMAR{} um triângulo.'.format(cores['vermelho'], cores['limpa']))