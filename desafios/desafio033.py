num = float(input('Digite o 1° número: '))

maior = 0

if num >= maior:
    maior = num

menor = maior

if num < menor:
    menor = num

print('>>> O maior número é o {:.2f}.'.format(maior))

print('>>> O menor número é o {:.2f}.'.format(menor))