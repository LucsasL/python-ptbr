# Diferentemente das Tuplas, as listas são facilmente mutáveis
num = [2, 5, 9, 1]

num[2] = 3
num.append(7)
num.sort()
num.insert(2, 0)

print(num)

# Podemos também inverter a ordem que a lista é mostrada
num.sort(reverse=True)
print(num)

print(f'\n... Essa lista tem {len(num)} elementos.')

# Podemos eliminar elementos também
num.pop()

print(num)