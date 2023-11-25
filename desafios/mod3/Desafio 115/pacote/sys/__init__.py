from time import sleep

from pacote import strings
from pacote import cores
from pacote import sys

cadastro = []
Pessoa = {}

def AnaliseEsc():
    while True:
        try:
            Esc = int(input('>>> Escolha: '))

        except ValueError:
            print(f'{cores.vermelho()}... [ERRO] Escolha inválida! Por favor, digite um número inteiro valido.{cores.padrão()}')

        else:
            if Esc == 1:
                Lista()

            elif Esc == 2:
                try:
                    strings.titulo('CADASTRAR NOVAS PESSOAS', 40)
                    Pessoa['NovPess'] = str(input('>>> Digite o nome: ')).strip().capitalize()
                    Pessoa['Idade'] = int(input(f'>>> Digite a idade de {Pessoa["NovPess"]}: '))

                except ValueError:
                    while True:
                        try:
                            Pessoa['Idade'] = int(input(f'>>> Idade Inválida! Digite um número inteiro valido: '))

                        except (ValueError, TypeError):
                            print(f'{cores.vermelho()}... [ERRO] Idade inválida! Digite um número inteiro valido.{cores.padrão()}')

                        else:
                            print(f'... Registro de {Pessoa["NovPess"]} adicionado com sucesso.')
                            cadastro.append(Pessoa.copy())
                            del Esc
                            break

                except KeyboardInterrupt:
                    print(f'... Você decidiu não digitar dados.')

                else:
                    print(f'... Registro de {Pessoa["NovPess"]} adicionado com sucesso.')
                    cadastro.append(Pessoa.copy())
                    del Esc
                
            elif Esc == 3:
                break

            else:
                print(f'{cores.vermelho()}... [ERRO] Não há {Esc}° escolha. Selecione uma opção valida: {cores.padrão()}')

        sleep(1)
        strings.menu()

    strings.titulo('VOLTE SEMPRE!')


def Lista():
    strings.titulo('PESSOAS CADASTRADAS', 40)
    for p in cadastro:
        print(f'{p["NovPess"]:30}{p["Idade"]} Anos')