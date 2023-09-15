vel = float(input('Digite a velocidade em que um carro está se locomovendo: '))

if vel > 80:
    div = (vel - 80) * 7
    print('>>> MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}.'.format(div))
else:
    print('>>> O carro está dentro da regularidade.')