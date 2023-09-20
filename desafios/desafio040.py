forms = {'limpa': '\033[m',
         'roxo': '\033[1;35m',
         'vermelho': '\033[1;31m',
         'amarelo': '\033[1;33m',
         'verde': '\033[1;32m'}

print('{}-=-{}'.format(forms['roxo'], forms['limpa']) * 20)
print('Teste para exame de escola')
print('{}-=-{}'.format(forms['roxo'], forms['limpa']) * 20)

aluno = str(input('Digite o nome do aluno: '))

n1 = float(input('Digite a primeira nota: '))

n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2) / 2

if m < 4.9:
    print('>>> Média: {}; {}ALUNO(A) REPROVADO!{}'.format(m, forms['vermelho'], forms['limpa']))
elif m >= 5 and m <= 6.9:
    print('>>> Média: {}; {}ALUNO(A) EM RECUPERAÇÃO!{}'.format(m, forms['amarelo'], forms['limpa']))
else:
    print('>>> Média: {}; {}ALUNO(A) APROVADO!{}'.format(m, forms['verde'], forms['limpa']))