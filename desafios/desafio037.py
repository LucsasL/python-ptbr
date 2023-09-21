forms = {'limpa': '\033[m',
         'bold': '\033[1m',
         'roxo': '\033[1;35m',
         'azul': '\033[34m'}

print('{}-=-{}'.format(forms['roxo'], forms['limpa']) * 20)
print('{}Conversor de números{}'.format(forms['bold'], forms['limpa']))
print('{}-=-{}'.format(forms['roxo'], forms['limpa']) * 20)

num = int(input('Digite um número inteiro: '))

print('''
[1] Converter para {}BINÁRIO{}
[2] Converter para {}OCTAL{}
[3] Converter para {}HEXADECIMAL{}'''.format(forms['bold'], forms['limpa'], forms['bold'], forms['limpa'], forms['bold'], forms['limpa']))

print('')
escolha = int(input('Qual será a base de conversão?: '))

if escolha == 1:
    print('>>> {} convertido para {}BINÁRIO{} é igual a {}'.format(num, forms['azul'], forms['limpa'], bin(num)[2:]))
elif escolha == 2:
    print('>>> {} convertido para {}OCTAL{} é igual a {}'.format(num, forms['azul'], forms['limpa'], oct(num)[2:]))
elif escolha == 3:
    print('>>> {} convertido para {}HEXADECIMAL{} é igual a {}'.format(num, forms['azul'], forms['limpa'], hex(num)[2:]))
else:
    print('>>> Opção inválida. Tente novamente.')