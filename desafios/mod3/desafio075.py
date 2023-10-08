par = nove = 0

for cont in range(0, 4):
    valor = float(input('>>> Digite um número: '))

    if valor == 9:
        nove += 1

    if valor % 2 == 0:
        par += 1

    valores = (valor, valor, valor, valor)

print(f'... Você digitou os valores: {valores}')

print(f'... O número 9 apareceu {nove} vezes.')

print(f'... O primeiro 3 foi digitado na posição {valores.index("3")}.')

print(f'... Os números pares digitados foram: {par}')