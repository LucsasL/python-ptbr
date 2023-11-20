# Declaração de variáveis
forms = (
    '\033[m',
    '\033[1m',
    '\033[1;40m',
    '\033[1;35m',
    '\033[31m'
)

# Funções
def Titulo(title):
    print(f'{forms[3]}-={forms[0]}' * 30)
    print(f'{forms[1]}{title}{forms[0]}'.center(60))
    print(f'{forms[3]}-={forms[0]}' * 30)

# Programa Principal