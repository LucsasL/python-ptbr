forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m',
    'azul': '\033[34m'
}

def Titulo(title):
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
    print(f'{forms["bold"]}{title}{forms["limpa"]}'.center(60))
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
    print()

def Escreva(msg):
    msgSize = len(msg) + 6
    print(f'{forms["roxo"]}~{forms["limpa"]}' * msgSize)
    print(f'{forms["bold"]}{msg}{forms["limpa"]}'.center(msgSize))
    print(f'{forms["roxo"]}~{forms["limpa"]}' * msgSize)

# Programa Principal
Titulo('ESCRITOR DE TEXTOS PERSONALIZADOS')
Escreva(str(input('>>> Digite uma mensagem a ser escrita: ')))