from time import sleep

from pacote import strings
from pacote import cores
from pacote.txt import *

opc = ('Ver pessoas cadastradas', 'Adicionar cadastro', 'Sair do sistema')
Pessoa = {}
arq = 'Cadastrados.txt'

def analiseEsc():
    while True:
        try:
            Esc = int(input('>>> Escolha: '))

        except ValueError:
            print(f'{cores.vermelho()}... [ERRO] Escolha inválida! Por favor, digite um número inteiro valido.{cores.padrão()}')

        else:
            if Esc == 1:
                lerArq()

            elif Esc == 2:
                try:
                    strings.titulo('CADASTRAR NOVAS PESSOAS')
                    Nome = str(input('>>> Digite o nome: ')).strip().capitalize()
                    Idade = int(input(f'>>> Digite a idade de {Nome}: '))

                except (ValueError, TypeError):
                    while True:
                        try:
                            Idade = int(input(f'>>> Idade Inválida! Digite um número inteiro valido: '))

                        except (ValueError, TypeError):
                            print(f'{cores.vermelho()}... [ERRO] Idade inválida! Digite um número inteiro valido.{cores.padrão()}')

                        else:
                            cadastrar(Nome, Idade, arq)
                            del Esc
                            break

                except KeyboardInterrupt:
                    print(f'... Você decidiu não digitar dados.')
                          
                else:
                    cadastrar(Nome, Idade)
                    del Esc
                
            elif Esc == 3:
                break

            else:
                print(f'{cores.vermelho()}... [ERRO] Não há {Esc}° escolha. Selecione uma opção valida: {cores.padrão()}')

        sleep(1)
        strings.menu(opc)

    strings.titulo('VOLTE SEMPRE!')

def cadastrar(nome = 'Desconhecido', idade = 0, arq = 'Cadastrados.txt'):
    try:
        a = open(arq, 'at')
    
    except:
        print('... Houve um ERRO na abertura do arquivo!')

    else:
        try:
            a.write(f'{nome};{idade:}\n')

        except:
            print(f'... Houve um ERRO na implementação dos dados.')

        else:
            print(f'... Registro de {nome} adicionado com sucesso.')

    finally:
        a.close()