n = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')

print('>>> Seu nome em maiúsculo é {}.\n'.format(n.upper))

print('>>> Seu nome em minúsculo é {}.\n'.format(n.lower()))

print('>>> Seu nome tem no total {} caracteres.\n'.format(len(n) - n.count(' ')))

print('>>> Seu primeiro nome tem {} caracteres.\n'.format(n.find(' ')))