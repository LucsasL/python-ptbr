forms = {
    'limpa': '\033[m',
    'bold': '\033[1n',
    'roxo': '\033[1;35m',
    'azul': '\033[34m',
    'amarelo': '\033[33m'
}

print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)
print('PAR OU ÍMPAR'.center(60))
print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)

numeros = []

par = []

impar = []

while True:
    num = int(input('>>> Digite um número: '))
    numeros.append(num)

    if num % 2 == 0:
        par.append(num)

    else:
        impar.append(num)

    resp = str(input('>>> Adicionar mais um número? [S / N]: ')).strip().upper()[0]

    if resp != 'S' and resp != 'N':
        while True:
            resp = str(input('>>> Valor inválido! Digite novamente [S / N]: ')).strip().upper()[0]

            if resp == 'S' or resp == 'N':
                break
        
        if resp == 'N':
            break

    elif resp == 'N':
        break

print('\n... Você digitou os valores: [ ', end='')

for item in range(len(numeros)):
    print(f'{forms["azul"] if item % 2 == 0 else forms["amarelo"]}{numeros[item]}{forms["limpa"]}', end=', ' if item < len(numeros) - 1 else ' ] \n')

print('-=-' * 20)
print(f'... Os valores ímpares foram: {forms["amarelo"]}{impar}{forms["limpa"]}')
print(f'... Os valores pares foram: {forms["azul"]}{par}{forms["limpa"]}')