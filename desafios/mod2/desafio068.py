from random import randint

forms = {'limpa': '\033[m',
         'bold': '\033[1m',
         'roxo': '\033[1;35m',
         'vermelho': '\033[31m',
         'verde': '\033[32m'}

jogven = 0

print('{}-=-{}'.format(forms['roxo'], forms['limpa']) * 20)
print('{}PAR OU ÍMPAR{}'.format(forms['bold'], forms['limpa']))
print('{}-=-{}'.format(forms['roxo'], forms['limpa']) * 20)

while True:
    jog = int(input('\n>>> Digite um número: '))

    PoI = str(input('>>> PAR ou ÍMPAR [P / I]: ')).strip().upper()[0]

    comp = randint(1, 20)

    s = jog + comp

    if s % 2 == 0:
        Res = '\033[34mPAR\033[m'
    else:
        Res = '\033[34mÍMPAR\033[m'

    if PoI == 'P' and s % 2 == 0:
        jogven += 1

        print(f'\n... O computador jogou {comp} e você jogou {jog}, somando os números jogados temos {s}, que é {Res}.')

        print('\n{}Você venceu!{} Vamos jogar novamente...'.format(forms['verde'], forms['limpa']))

    elif PoI == 'I' and s % 2 == 1:
        jogven += 1

        print(f'\n... O computador jogou {comp} e você jogou {jog}, somando os números jogados temos {s}, que é {Res}.')

        print('\n{}Você venceu!{} Vamos jogar novamente...'.format(forms['verde'], forms['limpa']))

    elif PoI == 'P' and s % 2 == 1:
        break

    elif PoI == 'I' and s % 2 == 0:
        break

    else:
        while PoI not in 'PI':
            PoI = str(input('Valor inválido! Digite novamente [P / I]: ')).strip().upper()[0]

            s = jog + comp

            if PoI == 'P' and s % 2 == 0:
                jogven += 1

                print(f'\n... O computador jogou {comp} e você jogou {jog}, somando os números jogados temos {s}, que é {Res}.')

                print('\n{}Você venceu!{} Vamos jogar novamente...'.format(forms['verde'], forms['limpa']))

            elif PoI == 'I' and s % 2 == 1:
                jogven += 1

                print(f'\n... O computador jogou {comp} e você jogou {jog}, somando os números jogados temos {s}, que é {Res}.')

                print('\n{}Você venceu!{} Vamos jogar novamente...'.format(forms['verde'], forms['limpa']))

            elif PoI == 'P' and s % 2 == 1:
                break

            elif PoI == 'I' and s % 2 == 0:
                break

        if PoI == 'P' and s % 2 == 1:
            break

        elif PoI == 'I' and s % 2 == 0:
            break

print(f'\n... O computador jogou {comp} e você jogou {jog}, somando os números jogados temos {s}, que é {Res}.')

print('\n... {}Você perdeu!{} Jogos vencidos: {}'.format(forms['vermelho'], forms['limpa'], jogven))