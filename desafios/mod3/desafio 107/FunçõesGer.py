# Importações
from desafio107 import forms

# funções externas
def Titulo(title):
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
    print(f'{forms["bold"]}{title}{forms["limpa"]}'.center(90))
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)