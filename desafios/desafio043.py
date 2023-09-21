forms = {'limpa': '\033[m',
         'bold': '\033[31m',
         'roxo': '\033[1;35m',
         'verde': '\033[32m',
         'vermelho': '\033[31m'}

print('{}-=-{}'.format(forms['roxo'], forms['limpa']) * 20)
print('Cálculo do IMC')
print('{}-=-{}'.format(forms['roxo'], forms['limpa']) * 20)

peso = float(input('Digite o peso [Kg]: '))

altura = float(input('Digite a altura [M]: '))

IMC = peso / (altura ** 2)

if IMC < 18.5:
    print('>>> Seu IMC: {:.2f}; Você está {}ABAIXO DO PESO.{}'.format(IMC, forms['vermelho'], forms['limpa']))
elif IMC >= 18.5 and IMC <= 25:
    print('>>> Seu IMC: {:.2f}; Você está {}PESO IDEAL.{}'.format(IMC, forms['verde'], forms['limpa']))
elif IMC > 25 and IMC <= 30:
    print('>>> Seu IMC: {:.2f}; Você está com {}SOBREPESO.{}'.format(IMC, forms['vermelho'], forms['limpa']))
elif IMC > 30 and IMC <= 40:
    print('>>> Seu IMC: {:.2f}; Você está {}OBESO.{}'.format(IMC, forms['vermelho'], forms['limpa']))
else:
    print('>>> Seu IMC: {:.2f}; Você está com {}OBESIDADE MÓRBIDA.{}'.format(IMC, forms['vermelho'], forms['limpa']))