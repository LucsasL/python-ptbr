i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)
print('FIM')

s = 0

for c in range(0, 10):
    num = int(input('Digite o {}° valor: '.format(c)))
    s = s + num
print(s)