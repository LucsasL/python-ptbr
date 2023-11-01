galera = [['Gustavo', 40], ['João', 17], ['Josué', 54], ['Tatia', 24]]
dado = list()
totmai = totmen = 0

for c in range(0, 5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))

print(' Dados de entrada '.center(40, '='))
for p in range(0, len(dado), 2):
    print(f'... {dado[p]} tem {dado[p + 1]} anos de idade.')

print(' Dados pre estabelecidos '.center(40, '='))
for p in galera:
    print(f'... {p[0]} tem {p[1]} anos de idade.')

print(' Maioridade? '.center(40, '='))
for p in galera:
    if p[1] >= 18:
        print(f'... {p[0]} é maior de idade.')
        totmai += 1

    else:
        print(f'... {p[0]} não é maior de idade.')
        totmen += 1

print(f'\n... Existem {totmai} pessoas que estão na maioridade e {totmen} que não estão')