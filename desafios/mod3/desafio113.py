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
        try:
            n = int(input(msg))

        except (ValueError, TypeError):
            print(f'{forms["vermelho"]}... [ERRO] Por favor, Digite um número inteiro válido.{forms["limpa"]}')

        except KeyboardInterrupt:
            print(f'{forms["vermelho"]}... O usuário preferiu não digitar o valor.{forms["limpa"]}')

            try:
                n = 0

            finally:
                return n

        else:
            return n

def LeiaFloat(msg):
    while True:
        try:
            n = float(input(msg))

        except (ValueError, TypeError):
            print(f'{forms["vermelho"]}... [ERRO] Por favor, digite um valor inteiro válido.{forms["limpa"]}')

        except KeyboardInterrupt:
            print(f'{forms["vermelho"]}... O usuário preferiu não digitar o valor.{forms["limpa"]}')
            
            try:
                n = 0

            finally:
                return n

        else:
            return n


# Programa Principal
Titulo('TRATAMENTO DE ERROS E EXCEÇÕES')

numInt = LeiaInt('>>> Digite um números Inteiro: ')
numFloat = LeiaFloat('>>> Digite um número Real: ')


print(f'... O número inteiro digitado foi o {numInt} e o número real foi {numFloat}.')