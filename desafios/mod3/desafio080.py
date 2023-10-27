forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m',
}

numeros = [0, 0, 0, 0, 0]

print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)
print('Desafio 80'.center(60))
print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)

for c in range(0, 5):
    num = float(input(f'>>> Digite o {c + 1}° número número: '))
    numeros.append(num)

    if numeros[c] < numeros[c - 1]:
        numeros.insert[0]
    
    if numeros[c] > numeros[c - 1]:
        numeros.insert[4]


print(numeros)