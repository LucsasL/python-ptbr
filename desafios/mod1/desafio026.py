frase = str(input('Digite uma frase: ')).strip().upper()

print('--------------------------------------')

print('>>> A letra A apareceu {} na frase.\n'.format(frase.count('A')))

print('>>> A primeira letra A apareceu na posição {}.\n'.format(frase.find('A') + 1))

print('>>> A últims letra A apareceu na posição {}.'.format(frase.rfind('A') + 1))