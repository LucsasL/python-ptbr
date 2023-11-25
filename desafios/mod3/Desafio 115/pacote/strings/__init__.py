from pacote import cores

def titulo(msg, tam = 20, char = '-='):
    '''
    Escreve um cabeçalho padronizado com cores.
    :msg: Texto do título
    :tam: Tamanho horizontal do título
    :char: Parametro opcional para aplicar estilo de título
    :return: Sem retorno de valores
    '''
    print(f'{cores.roxo()}{char}{cores.padrão()}' * 20)
    print(f'{cores.bold()}{msg}'.center(tam))
    print(f'{cores.roxo()}{char}{cores.padrão()}' * 20)

def menu():
    '''
    Escreve uma tabela de opções do usuário.
    '''
    titulo('MENU PRINCIPAL')
    print(f'{cores.azul()}{"[ 1 ] - ":7}{"Lista de cadastrados":25}')
    print(f'{"[ 2 ] - ":7}{"Cadastrar uma pessoa":25}')
    print(f'{"[ 3 ] - ":7}{"Sair do Sistema":25}{cores.padrão()}')
    print(f'{cores.roxo()}-={cores.padrão()}' * 20)