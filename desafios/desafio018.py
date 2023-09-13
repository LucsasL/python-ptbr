from math import radians, sin, cos, tan

ang = float(input('Digite um ângulo: '))

sen = sin(radians(ang))

cos = cos(radians(ang))

tan =  tan(radians(ang))

print('No ângulo de {} o seno é igual a {:.2f}, o cosseno igual a {:.2f} e a tangente igual a {:.2f}.'.format(ang, sen, cos, tan))