forms = {'limpa': '\033[m',
         'bold': '\033[1m',
         'roxo': '\033[1;35m',
         'azul': '\033[34m',
         'verde': '\033[32m',
         'vermelho': '\033[31m'}

print('{}-=-{}'.format(forms['roxo'], forms['limpa']) * 20)
print('{}Analisador de triângulos{}'.format(forms['bold'], forms['limpa']))
print('{}-=-{}'.format(forms['roxo'], forms['limpa']) * 20)

L1 = float(input('Digite o tamanho do primeiro lado: '))
L2 = float(input('Digite o tamanho do segundo lado: '))
L3 = float(input('Digite o tamanho do terceiri lado: '))

print('')

if L1 < L2 + L3 and L2 < L1 + L3 and L3 < L1 + L2:
    print('>>> Com as medidas apresentadas, {}É POSSÍVEL FORMAR{} UM {}TRIÂNGULO.{}'.format(forms['verde'], forms['limpa'], forms['azul'], forms['limpa']))
          
    if L1 == L2 and L2 == L3:
        print('>>> {}TRIÂNGULO EQUILÁTERO.{}'.format(forms['azul'], forms['limpa']))

    elif L1 != L2 and L2 != L3 and L3 != L1:
        print('>>> {}TRIÂNGULO ESCALENO.{}'.format(forms['azul'], forms['limpa']))

    else:
        print('>>> {}TRIÂNGULO ISÓSCELES.{}'.format(forms['azul'], forms['limpa']))
else:
    print('>>> Com as medidas dispostas, {}NÃO É POSSÍVEL FORMAR{} um triângulo.'.format(forms['vermelho'], forms['limpa']))