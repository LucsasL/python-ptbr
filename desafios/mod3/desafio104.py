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

def LeiaInt(input):
    if input == str():
        while True:
            print(f'{forms["vermelho"]}CÊ É BURRO CARA QUE LOUCURA.{forms["limpa"]}')

            if input == int():
                break
        
        else:
            return input

# Programa Principal
Titulo('INPUT EM FUNÇÕES')

num = LeiaInt('>>> Digite um números: ')

print(f'>>> Você digitou o número {num}')