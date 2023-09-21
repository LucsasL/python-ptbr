from random import randint

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

# Jogo acontecendo
if comp == 1 and jog == 2:
    jogador = True
    comp = 'PEDRA'

elif comp == 1 and jog == 3:    
    jogador = False
    comp = 'PEDRA'

elif comp == 1 and jog == 1:
    comp = 'PEDRA'
    jog = int(input('>>> {}EMPATE!{} O computador usou {}{}.{} Jogue de novo: '.format(forms['amarelo'], forms['limpa'], forms['amarelo'], comp, forms['limpa'])))

elif comp == 2 and jog == 3:
    jogador = True
    comp = 'PAPEL'

elif comp == 2 and jog == 1:
    jogador = False
    comp = 'PAPEL'

elif comp == 2 and jog == 2:
    comp = 'PAPEL'
    jog = int(input('>>> {}EMPATE!{} O computador usou {}{}.{} Jogue de novo: '.format(forms['amarelo'], forms['limpa'], forms['amarelo'], comp, forms['limpa'])))

elif comp == 3 and jog == 1:
    jogador = True
    comp = 'TESOURA'

elif comp == 3 and jog == 2:
    jogador = False
    comp = 'TESOURA'

else:
    comp = 'TESOURA'
    jog = int(input('>>> {}EMPATE!{} O computador usou {}{}.{} Jogue de novo: '.format(forms['amarelo'], forms['limpa'], forms['amarelo'], comp, forms['limpa'])))

# Verifica o estado do jogo
if jogador == False:
    print('>>> {}Você perdeu!{} O computador usou {}{}.{}\n'.format(forms['vermelho'], forms['limpa'], forms['amarelo'], comp, forms['limpa']))
else:
    print('>>> {}Você venceu!{} o computador usou {}{}.{}'.format(forms['verde'], forms['limpa'], forms['amarelo'], comp, forms['limpa']))