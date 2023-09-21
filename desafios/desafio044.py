forms = {'limpa': '\033[m',
         'bold': '\033[1m',
         'roxo': '\033[1;35m',
         'vermelho': '\033[31m',
         'azul': '\033[34m',
         'boldazul': '\033[1;34m',
         'amarelo': '\033[33m'}

print('{}-=-{}'.format(forms['roxo'], forms['limpa']) * 20)
print('{}preço do produto{}'.format(forms['bold'], forms['limpa']))
print('{}-=-{}'.format(forms['roxo'], forms['limpa']) * 20)

prod = float(input('{}Digite o valor do produto:{} {}R$'.format(forms['bold'],  forms['limpa'], forms['amarelo'])))

print('{}--------------'.format(forms['limpa']))
print('{}[1]{} Para pagar {}à vista {}(dinheiro ou cheque);{}'.format(forms['boldazul'], forms['limpa'], forms['bold'], forms['azul'], forms['limpa']))
print('{}[2]{} para pagar {}no cartão à vista {}(5% de desconto);{}'.format(forms['boldazul'], forms['limpa'], forms['bold'], forms['azul'], forms['limpa']))
print('{}[3]{} para pagar {}parcelado em 2x no cartão {}(preço normal);{}'.format(forms['boldazul'], forms['limpa'], forms['bold'], forms['azul'], forms['limpa']))
print('{}[4]{} para pagar {}parcelado em 3x ou mais no cartão. {}(20% de juros por parcela).{}'.format(forms['boldazul'], forms['limpa'], forms['bold'], forms['azul'], forms['limpa']))
print('')

pag = int(input('Digite a forma de pagamento: '))

if pag == 1:
    pag = 'À vista'
    print('>>> Método selecionado: {}{};{} Você deverá pagar: {}R${:.2f}'.format(forms['azul'], pag, forms['limpa'], forms['vermelho'], (prod - (prod * 0.1))))
elif pag == 2:
    pag = 'À vista no cartão'
    prod = prod - (prod * 0.05)
    print('>>> Método selecionado: {}{};{} Você deverá pagar: {}R${:.2f}'.format(forms['azul'], pag, forms['limpa'], forms['vermelho'], prod))
elif pag == 3:
    pag = '2x no cartão'
    print('>>> Método selecionado: {}{};{} Você deverá pagar: {}R${:.2f}{}. Sendo {}R${:.2f}{} em 2 parcelas.'.format(forms['azul'], pag, forms['limpa'], forms['vermelho'], prod, forms['limpa'], forms['vermelho'], (prod / 2), forms['limpa']))
else:
    parc = int(input('Quantas parcelas?: '))
    pag = '{}x no cartão'.format(parc)
    prod = prod + (prod * 0.2)
    print('>>> Método selecionado: {}{};{} Você deverá pagar: {}R${:.2f}{} ao todo. Sendo {}R${:.2f}{} em {} parcelas.'.format(forms['azul'], pag, forms['limpa'], forms['vermelho'], prod, forms['limpa'], forms['vermelho'], (prod / parc), forms['limpa'], parc))

    print(forms['limpa'])