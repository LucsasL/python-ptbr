# Importações
from pacote import string
from pacote import moedas
from pacote import cores

# Programa Principal
string.Titulo('MODULARIZAÇÃO EM PYTHON')

preço = float(input(f'>>> Digite o preço: {cores.Azul()}R$'))

print(f'{cores.Padrão()}... A metade de {moedas.moeda(preço, True)} é igual a {moedas.Metade(preço, True)}')
print(f'... O dobro de {moedas.moeda(preço, True)} é igual a {moedas.Dobro(preço, True)}')
print(f'... Aumentando 10%, temos {moedas.Aumentar(preço, 10, True)}')
print(f'... Reduzindo 13%, temos {moedas.Diminuir(preço, 13, True)}')