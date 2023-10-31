forms = {
    'limpa': '\033[m',
    'bold': '\033[1n',
    'roxo': '\033[1;35m',
    'azul': '\033[1;34m',
    'verde': '\033[32m',
    'vermelho': '\033[31m'
}

print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)
print('ANALISADOR DE ARRAYS'.center(60))
print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)

numeros = []

while True:
    numeros.append(int(input('>>> Digite um número: ')))

    resp = str(input('>>> Quer adicionar mais números? [S / N]: ')).strip().upper()[0]

    if resp != 'S' and resp != 'N':
        while True:
            resp = str(input('>>> Valor inválido! Digite novamente [S / N]: ')).strip().upper()[0]

            if resp == 'S' or resp == 'N':
                break
        
        if resp == 'N':
            break

    elif resp == 'N':
        break

numeros.sort(reverse=True)
print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)
print(f'... No total, foram digitados {len(numeros)} números.')
print(f'... A lista de números ordenadas é: {forms["azul"]}{numeros}{forms["limpa"]}')

if 5 in numeros:
    print(f'... o valor 5 {forms["verde"]}ESTÁ{forms["limpa"]} na lista.')

else:
    print(f'... O número 5 {forms["vermelho"]}NÃO ESTÁ{forms["limpa"]} na lista.')