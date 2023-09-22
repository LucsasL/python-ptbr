forms = {'limpa': '\033[m',
         'bold': '\033[1m',
         'roxo': '\033[1;35m'}

print('{}-=-{}'.format(forms['roxo'], forms['limpa']) * 20)
print('{}{:^5}{}'.format(forms['bold'], 'Números pares', forms['limpa']))
print('{}-=-{}'.format(forms['roxo'], forms['limpa']) * 20)

for c in range(0, 51, 2):
    print('... ', c)
print('... FIM!')