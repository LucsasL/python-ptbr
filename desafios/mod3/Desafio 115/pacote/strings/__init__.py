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

def menu(opc):
    '''
    Escreve uma tabela de opções do usuário.
    '''
    titulo('MENU PRINCIPAL')
    for i, o in enumerate(opc):
        print(f'{cores.azul()}[ {i + 1} ] - {o:25}{cores.padrão()}')
    linha()