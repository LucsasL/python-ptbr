forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m'
}

def Titulo(title):
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
    print(f'{title}'.center(60))
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)

def Contador(ini, fim, passo):
    """
    -> Faz uma contagem e mostra na tela.
    :param ini: Início da contagem
    :param fim: Fim da contagem
    :param passo: Passo da contagem
    :return: Sem retorno
    """
    for c in range(ini, fim, passo):
        print(f'{c} ', end='')
    print('FIM!')

def Somar(n1=0, n2=0, n3=0):
    soma = 0
    soma += n1 + n2 + n3
    return soma

def Teste():
    n = 5
    x = 8
    print(f'... Já na função Teste, o N vale {n}.')
    print(f'... Na função Teste, X vale {x}.')

def Função(b):
    global n1
    a = 8
    b += 3
    c = 5
    n1 = 89
    print(f'... A dentro vale {a}.')
    print(f'... B dentro vale {b}.')
    print(f'... C dentro vale {c}.')
    print(f'... N1 dentro vale {n1}.')

def Fatorial(num=1):
    for f in range(num - 1, 1, -1):
        num *= f
    return num

# Programa Principal
Titulo('DOCSTRINGS')

Contador(2, 10, 2)
help(Contador)

Titulo('PARAMETROS OPCIONAIS E RETURN')

r1 = Somar(3, 2, 5)
r2 = Somar(8, 4)
r3 = Somar()

print(f'... As primeiras repostas são {r1}, {r2} e {r3}.')

resp = Somar(3, 2, 5)
print(f'... A soma vale {resp}.')

Titulo('ESCOPOS')

n = 2

print(f'... No programa principal N vale {n}.')
Teste()

n1 = 2

Função(n1)
print(f'... N1 global vale {n1}')

Titulo('FATORIAL EM FUNÇÕES')

NumF = int(input('>>> Digite um número a ser fatorado: '))

print(f'... O Fatorial de {NumF} é igual a {Fatorial(NumF)}.')