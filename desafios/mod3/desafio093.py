forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m',
    'azul': '\033[34m'
}

jogos = {}

print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)
print(f'{forms["bold"]}CONDIÇÃO ALUNO{forms["limpa"]}'.center(60))
print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)

jogos['Nome'] = str(input('>>> Digite o nome do jogador: ')).strip().capitalize()
jogos['Partidas'] = int(input(f'>>> Quantas partidas {jogos["Nome"]} jogou: '))
jogos['Gols'] = []
jogos['Total'] = 0

for c in range(jogos['Partidas']):
    jogos['Gols'].append(int(input(f'>>> Quantos gols na partida {c + 1}?: ')))
    jogos['Total'] += jogos['Gols'][c]

print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
print(f'{jogos}')
print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)

for i, v in jogos.items():
    print(f'... O campo {forms["azul"]}{i}{forms["limpa"]} tem o valor {forms["azul"]}{v}.{forms["limpa"]}')

print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)

print(f'... O jogador {jogos["Nome"]} jogou {jogos["Partidas"]} partidas.')

for i, v in enumerate(jogos["Gols"]):
    print(f'    => Na partida {forms["azul"]}{i + 1},{forms["limpa"]} fez {forms["azul"]}{v} gols.{forms["limpa"]}')

print(f'... Foi um total de {forms["azul"]}{jogos["Total"]} gols.{forms["limpa"]}')