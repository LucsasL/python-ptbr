vel = float(input('Digite a velocidade em que um carro está se locomovendo: '))

cores = {'vermelho': '\033[1;31m',
         'limpa': '\033[m',
         'destaque': '\033[33m'}

if vel > 80:
    div = (vel - 80) * 7
    print('>>> {}MULTADO!{} Você excedeu o limite permitido que é de {}80Km/h{}'.format(cores['vermelho'], cores['limpa'], cores['destaque'], cores['limpa']))
    print('Você deve pagar uma multa de {}R${:.2f}{}.'.format(cores['vermelho'], div, cores['limpa']))
else:
    print('>>> O carro está dentro da regularidade.')