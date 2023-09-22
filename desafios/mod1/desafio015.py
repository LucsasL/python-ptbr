dias = int(input('Quantos dias alugado?: '))
km = float(input('Quantos Km rodados?: '))
preço = (km * 0.15) + (dias * 60)

print('O total a pagar é de R${:.2f}'.format(preço))