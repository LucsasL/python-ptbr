from time import sleep

from pacote import strings
from pacote import cores
from pacote import sys

cadastro = []
Pessoa = {}

def AnaliseEsc():
    while True:
        Esc = int(input('>>> Escolha: '))

        if Esc == 1:
            Lista()

        elif Esc == 2:
            try:
                strings.titulo('CADASTRAR NOVAS PESSOAS', 40)
                Pessoa['NovPess'] = str(input('>>> Digite o nome: ')).strip().capitalize()
                Pessoa['Idade'] = int(input(f'>>> Digite a idade de {Pessoa["NovPess"]}: '))

            except ValueError:
                Esc = int(input(f'[ERRO] Não há uma {Esc}° opção. Digite novamente: '))
                AnaliseEsc(Esc)

            except KeyboardInterrupt:
                print(f'... Você decidiu não digitar dados.')

            else:
                print(f'... Registro de {Pessoa["NovPess"]} adicionado com sucesso.')
                cadastro.append(Pessoa.copy())
                del Esc
            
        elif Esc == 3:
            break

        else:
            print(f'[ERRO] Não há {Esc}° escolha.')

        sleep(1)
        strings.menu()

    strings.titulo('VOLTE SEMPRE!')


def Lista():
    strings.titulo('PESSOAS CADASTRADAS', 40)
    for p in cadastro:
        print(f'{p["NovPess"]:30}{p["Idade"]} Anos')
    print(f'{cores.roxo()}-={cores.padrão()}' * 20)