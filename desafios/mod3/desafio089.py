forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m',
    'verde': '\033[1;32m'
}

print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)
print(f'{forms["bold"]}NOTAS DOS ALUNOS{forms["limpa"]}'.center(60))
print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)

alunos = []
alunoNotas = []
media = []
resp = ''
calcMedia = c = 0

while resp != 'N':
    alunoNotas.append(str(input('>>> Digite o nome: ')).strip().capitalize())
    alunoNotas.append(float(input('>>> Digite a 1° nota [0 / 10]: ')))
    alunoNotas.append(float(input('>>> Digite a 2° nota [0 / 10]: ')))
    alunos.append(alunoNotas[:])
    alunoNotas.clear()

    resp = str(input('>>> Adicionar outro aluno [S / N]: ')).strip().upper()[0]

    if resp != 'S' and resp != 'N':
        while True:
            resp = str(input('>>> Opção inválida! Digite novamente [S / N]: ')).strip().upper()[0]

            if resp == 'S' or resp == 'N':
                break

        if resp == 'N':
            break

for i in alunos:
    calcMedia += i[1] + i[2]
    media.append(calcMedia / 2)
    calcMedia = 0

print()
print(f' BOLETIM '.center(60, '='))
print(f'{"N.":4}{"NOME":50}{"MÉDIA"}')

print('-' * 60)

for i, m in enumerate(media):
    print(f'{i:<4}{alunos[c][0]:50}{media[c]:.1f}')
    c += 1

print('-' * 60)

print(f'>>> (999 para interromper programa) <<<')

while True:
    if len(alunos) == 1:
        mostra = str(input(f'>>> Mostrar notas do aluno? [S / N]: ')).strip().upper()[0]

        if mostra != 'S' and mostra != 'N':
            while True:
                mostra = str(input('>>> Opção inválida. Digite novamente [S / N]: ')).strip().upper()[0]

                if mostra == 'S' or mostra == 'N':
                    break
        
            if mostra == 'S':
                print(f'... Notas de {alunos[0][0]} são [{alunos[0][1]} {alunos[0][2]}]\n')
                break

            elif mostra == 'N':
                print('... FINALIZANDO...')
                break

        elif mostra == 'S':
            print(f'... Notas de {alunos[0][0]} são [{alunos[0][1]} {alunos[0][2]}]\n')
            break

        elif mostra == 'N':
            print('... FINALIZANDO...')
            break

    else:
        mostra = int(input(f'>>> Mostrar notas de qual aluno? [0 a {len(alunos) - 1}]: '))

        if mostra == 999:
            print('... FINALIZANDO...')
            break

        elif 0 <= mostra < len(alunos):
            print(f'... Notas de {alunos[mostra][0]} são [{alunos[mostra][1]} {alunos[mostra][2]}]\n')

        else:
            while True:
                mostra = int(input(f'>>> Índice inválido! Digite novamente [0 a {len(alunos) - 1}]: '))

                if 0 <= mostra < len(alunos):
                    print(f'... Notas de {alunos[mostra][0]} são [{alunos[mostra][1]} {alunos[mostra][2]}]\n')

                elif mostra == 999:
                    print('... FINALIZANDO...')
                    break

            if mostra == 999:
                break