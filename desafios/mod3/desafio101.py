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

def Voto(AnoNasc):
    '''
    -> Retorna Condição de voto nas eleições baseado na idade do indivíduo.
    :Param AnoNasc: Ano de nascimento do cidadão
    :Return: Retorna condição
    '''
    from datetime import date
    AnoAtual = date.today().year
    idade = AnoAtual - AnoNasc

    if idade < 16:
        return f'... Com {idade} anos o direito ao voto é {forms["vermelho"]}NEGADO.{forms["limpa"]}'
    
    elif idade < 18 or idade > 65:
        return f'... Com {idade} anos o direito ao voto é {forms["verde"]}OPCIONAL.{forms["limpa"]}'
    
    else:
        return f'... Com {idade} anos o dever/direito do voto é {forms["vermelho"]}OBRIGATÓRIO.{forms["limpa"]}'

# Programa Principal
Titulo('CONDIÇÃO DE VOTO')

print(Voto(int(input('>>> Digite seu ano de nascimento: '))))