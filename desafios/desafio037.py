forms = {'limpa': '\033[m',
         'bold': '\033[1m',
         'roxo': '\033[1;35m'}

print('{}-=-{}'.format(forms['roxo'], forms['limpa']) * 20)
print('{}Conversor de números{}'.format(forms['bold'], forms['limpa']))
print('{}-=-{}'.format(forms['roxo'], forms['limpa']) * 20)

num = int(input('Digite um número inteiro: '))

print('')
print('[1] Converter para {}Binário{}'.format(forms['bold'], forms['limpa']))
print('[2] Converter para {}Octal{}'.format(forms['bold'], forms['limpa']))
print('[3] Converter para {}Hexadecimal{}'.format(forms['bold'], forms['limpa']))

print('')
escolha = int(input('Qual será a base de conversão?: '))

if escolha == 1:
    print('teste')
elif escolha == 2:
    print('teste 2')
else:
    print('teste 3')