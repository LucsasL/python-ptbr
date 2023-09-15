sal = float(input('Digite o salário: R$'))

if sal > 1250.00:
    Nsal = sal + (sal * 0.10)
else:
    Nsal = sal + (sal * 0.15)

print('>>> O novo salário será de R${:.2f}.'.format(Nsal))