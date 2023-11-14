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

def Área(compr, larg):
    MQuad = compr * larg
    print(f'\n{forms["limpa"]}... O comprimento é {forms["azul"]}{compr:.2f}m{forms["limpa"]} e a largura é {forms["azul"]}{larg:.2f}m.{forms["limpa"]}')
    print(f'... Sendo assim, a área do terreno é igual {forms["azul"]}{MQuad:.2f}m².{forms["limpa"]}')

# Programa principal
Titulo('ÁREA DO RETÂNGULO')
Área(float(input(f'>>> Comprimento (M): {forms["azul"]}')), float(input(f'{forms["limpa"]}>>> Largura (m): {forms["azul"]}')))