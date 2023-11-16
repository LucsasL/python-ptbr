from datetime import date

forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
}

def Titulo(title):
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
    print(f'{forms["bold"]}{title}{forms["limpa"]}'.center(60))
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)

def CalcIdade(AnoNasc):
    '''
    -> Retorna Condição de voto nas eleições baseado na idade do indivíduo.
    :Param AnoNasc: Ano de nascimento do cidadão
    :Return: Retorna condição
    '''
    AnoAtual = date.today().year
    idade = AnoAtual - AnoNasc
    return idade

def Condição():
    if idade < 16:
        return f'{forms["vermelho"]}NEGADO.{forms["limpa"]}'
    
    elif idade < 18 or idade > 65:
        return f'{forms["verde"]}OPCIONAL.{forms["limpa"]}'
    
    else:
        return f'{forms["vermelho"]}OBRIGATÓRIO.{forms["limpa"]}'

# Programa Principal
Titulo('CONDIÇÃO DE VOTO')

idade = CalcIdade(int(input('>>> Digite seu ano de nascimento: ')))
Cond = Condição()

print(f'... Com {idade} anos, a condição de voto é {Cond}')