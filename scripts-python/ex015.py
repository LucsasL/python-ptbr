lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

# Sem posição, menos escrita
for comida in lanche:
    print(f'Eu vou comer {comida} ')

print('')

# Posição e item
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}.')

print('')

# Posição e item
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')

print('\nComi pra caramba!\n')

# Mostra itens da variável em ordem alfabetica
print(sorted(lanche))

a = (2, 5, 4)

b = (5, 8, 1, 2)

# A + B != B + A
print(a + b)
print(b + a)

del(b)

print(b)