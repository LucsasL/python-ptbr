import urllib
import urllib.request

forms = {
    'limpa': '\033[m',
    'verde': '\033[32m',
    'vermelho': '\033[31m'
}

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')

except urllib.error.URLError:
    print(f'''{forms["vermelho"]}
          O site Pudim não está acessível no momento.
          {forms["limpa"]}''')
else:
    print(f'''{forms["verde"]}
          Consegui acessar o site Pudim com sucesso!
          {forms["limpa"]}''')