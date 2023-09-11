prod = float(input('Qual o preço do produto?: R$'))
prodDes = prod * 0.95

print('O produto que antes custava R${:.2f}, passará a custar R${:.2f} com 5 por cento de desconto'.format(prod, prodDes))