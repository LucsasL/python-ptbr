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
calcMedia = 0

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

for n, i in alunos: # Erro ao tentar captar valor em uma sub-lista dentro de outra
    calcMedia += alunos[i] + alunos[i]
    media.append(calcMedia)
    calcMedia = 0

print(f' BOLETIM '.center(60, '='))
for a, i in alunos:
    print(f'{alunos[i]:10}{media[i]}')