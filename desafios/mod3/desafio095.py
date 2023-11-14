forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m',
    'azul': '\033[34m'
}

jogos = {}
jogadores = []
count = 0
resp = Escolha = ''

print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)
print(f'{forms["bold"]}AVALIAÇÃO DE JOGADORES{forms["limpa"]}'.center(60))
print(f'{forms["roxo"]}-=-{forms["limpa"]}' * 20)

while resp != 'N':
    if count > 0:
        print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
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
    
print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)

while Escolha != 999:
    # Índice de apenas 1 jogador
    if len(jogadores) == 1:
        Escolha = str(input('>>> Mostrar dados do jogador? [S / N]: ')).strip().upper()[0]

        if Escolha == 'S':
            print(f'- LEVANTAMENTOS DO JOGADOR {jogadores[0]["Nome"]}:')
            print(f'... O jogador {jogadores[0]["Nome"]} jogou {jogadores[0]["Partidas"]} partidas.')

            for i, v in enumerate(jogadores[0]["Gols"]):
                print(f'...    => Na partida {forms["azul"]}{i + 1},{forms["limpa"]} fez {forms["azul"]}{v} gols.{forms["limpa"]}')

            print(f'... Foi um total de {forms["azul"]}{jogadores[0]["Total"]} gols.{forms["limpa"]}')
            print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
            break
            
        elif Escolha == 'N':
            break
    
        else:
            while True:
                Escolha = str(input('>>> Opção inválida! Digite novamente [S / N]: ')).strip().upper()[0]

                if Escolha == 'N':
                    break

                elif Escolha == 'S':
                    print(f'- LEVANTAMENTOS DO JOGADOR {jogadores[0]["Nome"]}:')
                    print(f'... O jogador {jogadores[0]["Nome"]} jogou {jogadores[0]["Partidas"]} partidas.')

                    for i, v in enumerate(jogadores[0]["Gols"]):
                        print(f'...    => Na partida {forms["azul"]}{i + 1},{forms["limpa"]} fez {forms["azul"]}{v} gols.{forms["limpa"]}')

                    print(f'... Foi um total de {forms["azul"]}{jogadores[0]["Total"]} gols.{forms["limpa"]}')
                    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
                    break
            
            if Escolha == 'N':
                break

    # Multiplos índices
    else:
        Escolha = int(input(f'>>> Mostrar dados de qual jogador? [0 a {len(jogadores) - 1}]: '))

        if 0 <= Escolha < len(jogadores):
            print(f'- LEVANTAMENTOS DO JOGADOR {jogadores[Escolha]["Nome"]}:')
            print(f'... O jogador {jogadores[Escolha]["Nome"]} jogou {jogadores[Escolha]["Partidas"]} partidas.')

            for i, v in enumerate(jogadores[Escolha]["Gols"]):
                print(f'...    => Na partida {forms["azul"]}{i + 1},{forms["limpa"]} fez {forms["azul"]}{v} gols.{forms["limpa"]}')

            print(f'... Foi um total de {forms["azul"]}{jogadores[Escolha]["Total"]} gols.{forms["limpa"]}')
            print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
        
        elif Escolha == 999:
            break

        else:
            while True:
                Escolha = int(input(f'>>> Índice inválido! Digite novamente [0 e {len(jogadores) - 1}]: '))

                if 0 <= Escolha < len(jogadores):
                    print(f'- LEVANTAMENTOS DO JOGADOR {jogadores[Escolha]["Nome"]}:')
                    print(f'... O jogador {jogadores[Escolha]["Nome"]} jogou {jogadores[Escolha]["Partidas"]} partidas.')

                    for i, v in enumerate(jogadores[Escolha]["Gols"]):
                        print(f'...    => Na partida {forms["azul"]}{i + 1},{forms["limpa"]} fez {forms["azul"]}{v} gols.{forms["limpa"]}')

                    print(f'... Foi um total de {forms["azul"]}{jogadores[Escolha]["Total"]} gols.{forms["limpa"]}')
                    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
                    break

                elif Escolha == 999:
                    break

print('< VOLTE SEMPRE >'.center(60, '='))