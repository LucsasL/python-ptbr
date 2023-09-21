from random import randint

from time import sleep

forms = {'limpa': '\033[m',
         'bold': '\033[1m',
         'roxo': '\033[1;35m',
         'azul': '\033[1;34m',
         'amarelo': '\033[33m',
         'vermelho': '\033[31m',
         'verde': '\033[32m'}

print('{}-=-{}'.format(forms['roxo'], forms['limpa']) * 20)
print('J O K E N P Ô . . . ')
print('{}-=-{}'.format(forms['roxo'], forms['limpa']) * 20)

print('[1] PEDRA;')
print('[2] PAPEL;')
print('[3] TESOURA.')
print('')

jog = int(input('Pedra, Papel ou Tesoura?: '))

jogador = bool

comp = randint(1, 3)

print('JO')
sleep(.8)
print('KEN')
sleep(.8)
print('PÔ!!')
sleep(.8)

# Jogo acontecendo
if comp == 1:

    if jog == 1:
        comp = 'PEDRA'
        jog = int(input('>>> {}EMPATE!{} O computador usou {}{}.{} Jogue de novo: '.format(forms['amarelo'], forms['limpa'], forms['amarelo'], comp, forms['limpa'])))

        print('JO')
        sleep(.8)
        print('KEN')
        sleep(.8)
        print('PÔ!!')
        sleep(.8)

    elif jog == 2:
        jogador = True
        comp = 'PEDRA'

    elif jog == 3:    
        jogador = False
        comp = 'PEDRA'

    else:
        print('Jogada inválida, tente novamente.')

elif comp == 2:

    if jog == 1:
        jogador = False
        comp = 'PAPEL'

    elif jog == 2:
        comp = 'PAPEL'
        jog = int(input('>>> {}EMPATE!{} O computador usou {}{}.{} Jogue de novo: '.format(forms['amarelo'], forms['limpa'], forms['amarelo'], comp, forms['limpa'])))

        print('JO')
        sleep(.8)
        print('KEN')
        sleep(.8)
        print('PÔ!!')
        sleep(.8)
    
    elif jog == 3:
        jogador = True
        comp = 'PAPEL'

    else:
        print('Jogada inválida, tente novamente.')
    
elif comp == 3:

    if jog == 1:
        jogador = True
        comp = 'TESOURA'

    elif jog == 2:
        jogador = False
        comp = 'TESOURA'

    elif jog == 3:
        comp = 'TESOURA'
        jog = int(input('>>> {}EMPATE!{} O computador usou {}{}.{} Jogue de novo: '.format(forms['amarelo'], forms['limpa'], forms['amarelo'], comp, forms['limpa'])))

        print('JO')
        sleep(.8)
        print('KEN')
        sleep(.8)
        print('PÔ!!')
        sleep(.8)

    else:
        print('Jogada inválida, tente novamente.')

# Verifica o estado do jogo

if jog == 1:
    print('Jogada: {}'.format(jog))
elif jog == 2:
    print('Jogada: {}'.format(jog))
else:
    print('Jogada: {}'.format(jog))

if jogador == False:
    print('>>> {}Você perdeu!{} O computador usou {}{}.{}\n'.format(forms['vermelho'], forms['limpa'], forms['amarelo'], comp, forms['limpa']))
else:
    print('>>> {}Você venceu!{} o computador usou {}{}.{}'.format(forms['verde'], forms['limpa'], forms['amarelo'], comp, forms['limpa']))