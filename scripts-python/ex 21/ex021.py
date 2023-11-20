# Importações
from uteis import números
from uteis import strings

# Programa Principal
strings.Titulo('MODULARIZAÇÃO EM PYTHON')
num = int(input('>>> Digite um número: '))
fat = números.Fatorial(num)
print(f'... O fatorial de {num} é igual a {fat}.')
print(f'... Já o dobro de {num} é {números.Dobro(num)}, e o triplo de {num} é {números.Triplo(num)}.')