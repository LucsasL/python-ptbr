forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m',
    'azul': '\033[34m'
}

jogos = {}
jogadores = []
count = 0
resp = ''

print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)
print(f'{forms["bold"]}CONDIÇÃO ALUNO{forms["limpa"]}'.center(60))
print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)

while resp != 'N':
    if count > 0:
        print(f'{forms["roxo"]}-{forms["limpa"]}' * 60)
    jogos['Nome'] = str(input('>>> Digite o nome do jogador: ')).strip().capitalize()
    jogos['Partidas'] = int(input(f'>>> Quantas partidas {jogos["Nome"]} jogou: '))
    jogos['Gols'] = []
    jogos['Total'] = 0

    for c in range(jogos['Partidas']):
        jogos['Gols'].append(int(input(f'>>> Quantos gols na partida {c + 1}?: ')))
        jogos['Total'] += jogos['Gols'][c]

    jogadores.append(jogos.copy())
    count += 1

    resp = str(input('>>> Adicionar mais um jogador [S / N]: ')).strip().upper()[0]

    if resp != 'S' and resp != 'N':
        while True:
            resp = str(input('>>> Opção inválida! Digite novamente [S / N]: ')).strip().upper()[0]

            if resp == 'S' or resp == 'N':
                break

print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
print(f'{"Ind.":<5}{"Nome":<30}{"Gols":<20}{"Total":>5}')
print(f'{forms["roxo"]}-{forms["limpa"]}' * 60)

for i, v in enumerate(jogadores):
    print(f'{i:<5}{v["Nome"]:<30}{v["Gols"]}{v["Total"]:>5}')

Escolha = int(input(f'>>> Mostrar dados de qual jogador? [0 a {len(jogadores) - 1}]: '))

'''print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
print(f'{jogos}')
print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)

for i, v in jogos.items():
    print(f'... O campo {forms["azul"]}{i}{forms["limpa"]} tem o valor {forms["azul"]}{v}.{forms["limpa"]}')

print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)

print(f'... O jogador {jogos["Nome"]} jogou {jogos["Partidas"]} partidas.')

for i, v in enumerate(jogos["Gols"]):
    print(f'    => Na partida {forms["azul"]}{i + 1},{forms["limpa"]} fez {forms["azul"]}{v} gols.{forms["limpa"]}')

print(f'... Foi um total de {forms["azul"]}{jogos["Total"]} gols.{forms["limpa"]}')'''