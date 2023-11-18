# Declaração de variáveis
resp = ''

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

def Ajuda(doc, cor = forms[0]):
    Titulo(f'ACESSANDO DOCUMENTAÇÃO "{doc}"')
    print(cor, end='')
    help(doc)
    print(forms[0])

# Programa Principal
Titulo('SISTEMA DE AJUDA PyHELP')

while True:
    resp = str(input(f'>>> Função ou Biblioteca {forms[4]}[FIM para finalizar]{forms[0]}: ')).strip()

    if resp.upper() != 'FIM':
        Ajuda(resp, forms[2])
        print(resp)
    
    else:
        break