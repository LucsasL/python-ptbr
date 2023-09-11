alt = float(input('O quão alta é sua parede? [M]: '))
lar = float(input('Quantos comprimentos? [M]: '))
area = alt * lar
QuantL = (area / 2)

print('A área de sua parede é de {}M. Serão necessárias {} litros de tinta para pinta-la completamente.'.format(area, QuantL))