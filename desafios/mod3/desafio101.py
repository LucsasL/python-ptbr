from datetime import date

forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m',
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
    AnoAtual = date.today().year
    idade = AnoAtual - AnoNasc

    if idade < 16:
        return 'NEGADO'
    
    elif idade < 18:
        return 'OPCIONAL'
    
    else:
        return 'OBRIGATÓRIO'

# Programa Principal
Titulo('CONDIÇÃO DE VOTO')

Cond = Voto(int(input('>>> Digite seu ano de nascimento: ')))

print(f'... A condição de voto é {Cond}.')