n = str(input('Digite seu nome completo: ')).strip()

nome = n.split()

print('>>> Muito prazer em conhecer!\n')

print('>>> Seu primeiro nome é: {}\n'.format(nome[0]))

print('>>> Seu último nome é: {}.'.format(nome[len(nome) - 1]))