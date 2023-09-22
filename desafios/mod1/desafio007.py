nome = str(input('Nome do aluno: '))
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = float((n1 + n2) / 2)

print('>>> Nota 1: {}\n>>> Nota 2: {}'.format(n1, n2))

print('>>> A média do aluno {} foi {:.1f}.'.format(nome, m))