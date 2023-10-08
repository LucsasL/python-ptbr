palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

vogais = ('A', 'E', 'I', 'O', 'U')

for cont in palavras:

    contA = palavras[cont].count('A')

    contE = palavras[cont].count('E')

    contI = palavras[cont].count('I')

    contO = palavras[cont].count('O')

    contU = palavras[cont].count('U')

    print(f'\n... Na palavra {palavras[cont]} temos as vogais:', end=' ')

    if contA >= 1:
        print(f'{vogais[0]}', end=' ')

    if contE >= 1:
        print(f'{vogais[1]}', end=' ')

    if contI >= 1:
        print(f'{vogais[2]}', end=' ')

    if contO >= 1:
        print(f'{vogais[3]}', end=' ')

    if contU >= 1:
        print(f'{vogais[4]}', end=' ')

    cont += 1