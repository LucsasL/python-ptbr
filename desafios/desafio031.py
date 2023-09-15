DisViag = float(input('Digite a distância da viagem [Km]: '))

if DisViag <= 200:
    Pass = DisViag * 0.5
else:
    Pass = DisViag * 0.45

print('A passagem custará R${:.2f}.'.format(Pass))