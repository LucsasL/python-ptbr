print('-=-' * 20)
print('Analisador de triângulos')
print('-=-' * 20)

L1 = float(input('Digite o tamanho do primeiro lado: '))
L2 = float(input('Digite o tamanho do segundo lado: '))
L3 = float(input('Digite o tamanho do terceiri lado: '))

if L1 < L2 + L3 and L2 < L1 + L3 and L3 < L1 + L2:
    print('>>> Com as medidas apresentadas, É POSSÍVEL FORMAR um triângulo.')

else:
    print('>>> Com as medidas dispostas, NÃO É POSSÍVEL FORMAR um triângulo.')