forms = {
    'limpa': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m'
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
    mediaTurma = 0
    for i, n in enumerate(notas):
        mediaTurma += n

        if i == 0:
            maior = menor = n
        
        if n > maior:
            maior = n

        if n < menor:
            menor = n

    mediaTurma /= len(notas)
    alunos['Total de Notas'] = len(notas)
    alunos['Maior Nota'] = maior
    alunos['Menor Nota'] = menor
    alunos['Media da Sala'] = f'{mediaTurma:.2f}'

    if sit == True:
        if mediaTurma < 5:
            alunos['sit'] = 'RUIM'

        elif mediaTurma < 7:
            alunos['sit'] = 'RAZOÁVEL'

        else:
            alunos['sit'] = 'BOA'

    return alunos

# Programa Principal
Titulo('NOTAS DOS ALUNOS')
resp = Notas(5.5, 9.5, 10, 6.5, 7, 3, 1, 3.5, sit = True)
print(resp)
help(Notas)