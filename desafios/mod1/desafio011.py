lar = float(input('Qual a largura de sua parede? [M]: '))
alt = float(input('O quão alta é sua parede? [M]: '))
area = alt * lar
QuantL = float(area / 2)

print('>>> As dimensões de sua parede são {}x{}, tendo área de {}m². Serão necessários {} litros de tinta para pinta-la completamente.'.format(lar, alt, area, QuantL))