a = float(input('Digite o 1° número: '))

b = float(inpur('Digite o 2° número: '))

c = float(inpur('Digite o 3° número: '))

maior = a
# Número maior
if b > a and b > c:
    maior = b

if c > a and c > b:
    maior = c

menor = a
# Número menor
if b < a and b < c:
    menor = b

if c < a and c < b:
    menor = c

print('>>> O maior número é o {:.2f}.'.format(maior))

print('>>> O menor número é o {:.2f}.'.format(menor))