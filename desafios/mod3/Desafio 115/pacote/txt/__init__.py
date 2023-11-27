from pacote.strings import *

def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    
    except FileNotFoundError:
        return False
    
    else:
        return True
    
def criarArq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()

    except:
        print('... Houve um erro na criação do arquivo!')

    else:
        print(f'... Arquivo {nome} criado com sucesso!')

def lerArq(nome = 'Cadastrados.txt'):
    try:
        a = open(nome, 'rt')
    
    except:
        print('... Erro ao ler o arquivo.')
    
    else:
        titulo('PESSOAS CADASTRADAS')
        print(f'{"Ind.":5}{"Nome":45}{"Idade":^10}')
        linha(60, '-')
        for i, p in enumerate(a):
            print(f'{i:5}{a.readlines():45}{f"{a.readlines():^10} anos"}')