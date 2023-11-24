forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m',
    'vermelho': '\033[31m'
}

def Titulo(title):
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
    print(f'{forms["bold"]}{title}{forms["limpa"]}'.center(60))
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)

def LeiaInt(msg):
    n = msg
    while True:
        n = str(input(msg))

        if n.isnumeric():
            valor = int(n)
            break

        else:
            try Exception:
                print(f'{forms["vermelho"]}[ERRO] Digite um número inteiro válido.{forms["limpa"]}')

            except ellipsis:
                print()

            else:
                print()
    
    return valor
        
# Programa Principal
Titulo('INPUT EM FUNÇÕES')

num = LeiaInt('>>> Digite um números: ')

print(f'>>> Você digitou o número {num}.')