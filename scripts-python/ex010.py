a = 3

b = 5

cores = {'limpa': '\033[m',
         'verde': '\033[1;32m',
         'vermelho': '\033[1;31m',
         'pretoebranco': '\033[7;1m'}

print('\033[1;35m-=-' * 10)
print('\033[1;37m      Cores no Terminal   ')
print('\033[1;35m-=-' * 10)

print('\033[37;45mHello, World!\033[0;37m\n')

print('{}>>> Esse é um programa para testar cores no terminal!{}\n'.format(cores['pretoebranco'], cores['limpa']))

print('A variável {}{}{} e {}{}{}.'.format(cores['verde'], a, cores['limpa'], cores['vermelho'], b, cores['limpa']))