par = 0

valores = (float(input('>>> Digite um número: ')), float(input('>>> Digite outro número: ')), float(input('>>> Digite mais um número: ')), float(input('>>> Digite o último número: ')))

print(f'... Você digitou os valores: {valores}')

print(f'... O número 9 apareceu {valores.count(9)} vezes.')

if 3 in valores:
    print(f'... O primeiro 3 foi digitado na posição {valores.index(3) + 1}.')
else:
    print('O número 3 não foi digitado na tupla.')

for n in valores:
    if n % 2 == 0:
        par += 1

print(f'... Os números pares digitados foram: {par}')