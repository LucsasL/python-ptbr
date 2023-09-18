sal = float(input('Digite o salário: R$'))

if sal > 1250.00:
    Nsal = sal + sal * 0.10
else:
    Nsal = sal + sal * 0.15

cores = {'limpa': '\033[m',
         'verde': '\033[1;32m'}

print('>>> O novo salário será de {}R${:.2f}.{}'.format(cores['verde'], Nsal, cores['limpa']))