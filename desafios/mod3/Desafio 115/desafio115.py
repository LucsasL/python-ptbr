from pacote.strings import *
from pacote.sys import analiseEsc
from pacote.txt import *

# Programa Principal
arq = 'Cadastrados.txt'
opc = ('Ver pessoas cadastradas', 'Adicionar cadastro', 'Sair do sistema')

if arqExiste(arq):
    print(f'... Arquivo "{arq}" encontrado com sucesso.')

else:
    print('... Arquivo não encontrado.')
    criarArq(arq)

menu(opc)
analiseEsc()