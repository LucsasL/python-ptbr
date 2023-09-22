midade = 0

mm20 = 0

maioridade = 0

nomem = str

for c in range(1, 5):
    nome = str(input('\n>>> Digite o nome da {}° pessoa: '.format(c)))
    idade = int(input('>>> Digite a idade da {}° pessoa: '.format(c)))
    sexo = str(input('>>> Digite o sexo da {}° pessoa [M / F]: '.format(c)).upper())

    midade += idade

    if idade > maioridade:
        maioridade = idade

    if sexo == 'M' and idade > maioridade:
        nomem = nome

    if sexo == 'F' and idade < 20:
        mm20 += 1

midade = midade / c

print('\n... MÉDIA DE IDADE ENTRE AS PESSOAS: {}'.format(midade))
print('... NOME DO HOMEM MAIS VELHO: {}'.format(nomem))
print('... QUANTIDADE DE MULHERES COM MENOS DE 20 ANOS: {}'.format(mm20))