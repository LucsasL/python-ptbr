import 

forms = {
    'limpa': '\033[m',
    'verde': '\033[32m',
    'vermelho': '\033[31m'
}

try:
    print(f'{forms["verde"]}Consegui acessar o site Pudim com sucesso!{forms["limpa"]}')

except:
    print(f'{forms["vermelho"]}O site Pudim não está acessível no momento.{forms["limpa"]}')