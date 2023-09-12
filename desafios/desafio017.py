CO = float(input('Qual o comprimento do cateto oposto?: '))

CA = float(input('Qual o comprimento do cateto adjacente?: '))

H = (CA ** 2 + CO ** 2) ** (1/2)

print('Em um triângulo retângulo com cateto oposto de {}cm e cateto adjacente de {}cm, a hipotenusa é de {:.2f}cm.'.format(CO, CA, H))