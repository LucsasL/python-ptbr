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
        i = 1
    
    except:
        print('... Erro ao ler o arquivo.')
    
    else:
        i += 1
        titulo('PESSOAS CADASTRADAS')
        print(f'{"Ind.":5}{"Nome":45}{"Idade":^10}')
        linha(60, '-')
        for i, linhas in enumerate(a):
            dado = linhas.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{i + 1:^5}{dado[0]:<45}{dado[1]:} anos')
        
    finally:
        a.close()