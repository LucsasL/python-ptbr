forms = {'limpa': '\033[m',
         'bold': '\033[1m',
         'roxo': '\033[1;35m'}

print('{}-=-{}'.format(forms['roxo'], forms['limpa']) * 20)
print('{}Comparador de números{}'.format(forms['bold'], forms['limpa']))
print('{}-=-{}'.format(forms['roxo'], forms['limpa']) * 20)

num1 = int(input('Digite um número: '))

num2 = int(input('Digite outro número: '))

if num1 > num2:
    print('O número {} é maior.'.format(num1))
elif num1 == num2:
    print('Não há diferença entre os dois números digitados.')
else:
    print('O número {} é maior.').format(num2)