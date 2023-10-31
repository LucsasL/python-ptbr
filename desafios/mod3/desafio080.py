forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m',
}

print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)
print('ORGANIZADOR DE LISTA SEM USO DO SORT'.center(60))
print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)

numeros = []

for c in range(0, 5):
    num = int(input(f'>>> Digite o {c + 1}° número número: '))

    if c == 0 or num > numeros[-1]:
        print('... Número adicionado na posição final da lista...')
        numeros.append(num)
    
    else:
        pos = 0
        while pos < len(numeros):
            if num <= numeros[pos]:
                print(f'... Número posicionado no índice {pos} da lista...')
                numeros.insert(pos, num)
                break
            pos += 1

print('-=-' * 30)
print(f'... Os valores digitados em ordem foi {numeros}.')