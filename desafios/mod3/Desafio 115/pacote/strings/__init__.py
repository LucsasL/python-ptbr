from pacote import cores

def linha(tam = 30, char = '-='):
    '''
    Escreve uma linha com tamanho e caracteres personalizaveis.
    :tam: Configura o tamanho da linha
    :char: Configura os caracteres que formaram a linha
    :return: Retorna a linha com os parametros configurados acima.
    '''
    print(f'{cores.roxo()}{char}{cores.padrão()}' * tam)

def titulo(msg, tam = 60):
    '''
    Escreve um cabeçalho padronizado com cores.
    :msg: Texto do título
    :tam: Tamanho horizontal do título
    :return: Sem retorno de valores
    '''
    linha()
    print(f'{cores.bold()}{msg}'.center(tam))
    linha()

def menu():
    '''
    Escreve uma tabela de opções do usuário.
    '''
    titulo('MENU PRINCIPAL')
    print(f'{cores.azul()}{"[ 1 ] - ":7}{"Lista de cadastrados":25}')
    print(f'{"[ 2 ] - ":7}{"Cadastrar uma pessoa":25}')
    print(f'{"[ 3 ] - ":7}{"Sair do Sistema":25}{cores.padrão()}')
    linha()