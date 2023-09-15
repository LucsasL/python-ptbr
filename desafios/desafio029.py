vel = float(input('Digite a velocidade em que um carro está se locomovendo: '))

if vel > 80:
    div = (vel - 80) * 7
    print('O carro está mutado! Page a dívida de R${:.2f}.'.format(div))
else:
    print('O carro está dentro da regularidade.')