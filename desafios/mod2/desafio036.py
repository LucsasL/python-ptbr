cores = {'limpa': '\033[m',
         'bold': '\033[1m',
         'vermelho': '\033[1;31m',
         'amarelo': '\033[1;33m',
         'verde': '\033[1;32m',
         'roxo': '\033[1;35m'}

casa = float(input('Digite o valor da casa: {}R$'.format(cores['amarelo'])))

sal = float(input('{}Qual o valor do seu salário?: {}R$'.format(cores['limpa'], cores['amarelo'])))

ano = int(input('{}Em quantos anos você pretende pagar tudo?: '.format(cores['limpa'])))

empre = casa / (ano * 12)

print('VALOR DAS PRESTAÇÕES {}R${:.2f}.{}'.format(cores['vermelho'], empre, cores['limpa']))

# Não precisa de condicionais aninhadas
if empre <= sal * 0.3:
    print('{}Empréstimo realizado!{}'.format(cores['verde'], cores['limpa']))
else:
    print('{}Não será possível realizar o empréstimo!{} O valor das prestações ({:.2f}) ultrapassam {}30%{} do salário ({:.2f}).'.format(cores['vermelho'], cores['limpa'], empre, cores['amarelo'], cores['limpa'], (sal * 0.3)))