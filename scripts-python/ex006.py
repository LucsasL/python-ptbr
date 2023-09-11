n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
mo = n1 % n2

print('---------------------------\n>>> PRIMEIRO NÚMERO: {};\n>>> SEGUNDO NÚMERO: {}.\n---------------------------\n'.format(n1, n2))

print('>>> A soma entre {} e {} vale {};\n\n>>> A subtração entre {} e {} é igual a {};\n\n>>> A multiplicação entre {} e {} é igual a {};\n\n>>> A divisão entre {} e {} é igual a {};\n\n>>> A divisão inteira entre {} e {} é igual a {};\n\n>>> A potência entre {} e {} é igual a {};\n\n>>> O resto da divisão entre {} e {} é igual a {}.'.format(n1, n2, s, n1, n2, su, n1, n2, m, n1, n2, d, n1, n2, di, n1, n2, e, n1, n2, mo))