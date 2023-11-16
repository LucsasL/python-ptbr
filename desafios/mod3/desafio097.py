forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m',
}

def Titulo(title):
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
    print(f'{forms["bold"]}{title}{forms["limpa"]}')
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)

def Escreva(msg):
    msgSize = len(msg) + 4
    print(f'{forms["roxo"]}~{forms["limpa"]}' * msgSize)
    print(f'  {forms["bold"]}{msg}{forms["limpa"]}'.center(msgSize))
    print(f'{forms["roxo"]}~{forms["limpa"]}' * msgSize)

# Programa Principal
Titulo('ESCRITOR DE TEXTOS PERSONALIZADOS')
Escreva(str(input('>>> Digite uma mensagem a ser escrita: ')))