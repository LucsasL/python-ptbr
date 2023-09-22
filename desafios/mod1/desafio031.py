DisViag = float(input('Digite a distância da viagem [Km]: '))

cores = {'amarelo': '\033[33m', 'limpa': '\033[m'}

if DisViag <= 200:
    Pass = DisViag * 0.5
else:
    Pass = DisViag * 0.45

print('A passagem custará {}R${:.2f}.{}'.format(cores['amarelo'], Pass, cores['limpa']))