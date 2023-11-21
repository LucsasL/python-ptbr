# Importações
from pacote import string
from pacote import moedas
from pacote import cores
from pacote import dado

# Programa Principal
string.Titulo('MODULARIZAÇÃO EM PYTHON')
preço = dado.LeiaDinheiro()

print(preço)
'''moedas.Resumo(preço, 80, 33)'''