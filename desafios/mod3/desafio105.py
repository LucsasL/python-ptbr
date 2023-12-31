forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m'
}

def Titulo(title):
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)
    print(f'{forms["bold"]}{title}{forms["limpa"]}'.center(60))
    print(f'{forms["roxo"]}-={forms["limpa"]}' * 30)

def Notas(* notas, sit = False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param notas: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: Dicionário com várias informações sobra a situação da turma
    '''
    alunos = {}
    alunos['Total de Notas'] = len(notas)
    alunos['Maior Nota'] = max(notas)
    alunos['Menor Nota'] = min(notas)
    alunos['Media da Sala'] = sum(notas) / len(notas)

    if sit:
        if alunos['Media da Sala'] < 5:
            alunos['sit'] = 'RUIM'

        elif alunos['Media da Sala'] < 7:
            alunos['sit'] = 'RAZOÁVEL'

        else:
            alunos['sit'] = 'BOA'

    return alunos

# Programa Principal
Titulo('NOTAS DOS ALUNOS')
resp = Notas(5.5, 9.5, 10, 6.5, 7, 3, 1, 3.5, sit = True)
print(resp)
help(Notas)