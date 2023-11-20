# Importações
from pacote import string
from pacote import moedas
from pacote import cores

# Programa Principal
string.Titulo('MODULARIZAÇÃO EM PYTHON')

preço = float(input(f'>>> Digite o preço: {cores.Azul()}R$'))
print(f'{cores.Padrão()}... A metade de {cores.Azul()}R${preço:.2f}{cores.Padrão()} é igual a {cores.Azul()}R${moedas.Metade(preço):.2f}.{cores.Padrão()}')
print(f'... O dobro de {cores.Azul()}R${preço:.2f}{cores.Padrão()} é igual a {cores.Azul()}R${moedas.Dobro(preço):.2f}.{cores.Padrão()}')
print(f'... Aumentando 10%, temos {cores.Azul()}R${moedas.Aumentar(preço, 10):.2f}.{cores.Padrão()}')
print(f'... Reduzindo 13%, temos {cores.Azul()}R${moedas.Diminuir(preço, 13):.2f}.{cores.Padrão()}')