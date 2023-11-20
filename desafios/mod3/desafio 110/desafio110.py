# Importações
from pacote import string
from pacote import moedas
from pacote import cores

# Programa Principal
string.Titulo('MODULARIZAÇÃO EM PYTHON')

preço = float(input(f'>>> Digite o preço: {cores.Azul()}R$'))
moedas.Resumo(preço, 80, 33)