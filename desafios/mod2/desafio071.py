uniced = dezced = vinced = cinced = 0

print('=' * 35)
print('{:^35}'.format(' SACAR NO BANCO '))
print('=' * 35)

din = int(input('>>> Digite o valor a sacar: R$'))

total = din

while total >= 50:
    cinced += 1
    total -= 50

while total >= 20:
    vinced += 1
    total -= 20

while total >= 10:
    dezced += 1
    total -= 10

while total >= 1:
    uniced += 1
    total -= 1

print('=' * 35)

if cinced >= 1:
    print(f'... Total de {cinced} cédulas de R$50')

if vinced >= 1:
    print(f'... Total de {vinced} cédulas de R$20')

if dezced >= 1:
    print(f'... Total de {dezced} cédulas de R$10')

if uniced >= 1:
    print(f'... Total de {uniced} cédulas de R$1')

print('=' * 35)

print('Volte sempre e tenha um bom dia!')