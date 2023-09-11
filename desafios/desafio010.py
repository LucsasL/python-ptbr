reais = float(input('Quantos reais você tem?: R$'))
dol = float(reais / 5.20)

print('Com R${:.2f} vocé pode comprar US${:.2f}.'.format(reais, dol))