forms = {'limpa': '\033[m',
         'bold': '\033[1m',
         'roxo': '\033[1;35m',
         'amarelo': '\033[33m'}

print('{}-=-{}'.format(forms['roxo'], forms['limpa']) * 20)
print('{}Analisador de idade{}'.format(forms['bold'], forms['limpa']))
print('{}-=-{}'.format(forms['roxo'], forms['limpa']) * 20)

idade = int(input('Digite a idade do atleta: '))

if idade <= 9:
    print('Atleta {}MIRIM.{}'.format(forms['amarelo'], forms['limpa']))
elif idade <= 14:
    print('Atleta {}INFANTIL.{}'.format(forms['amarelo'], forms['limpa']))
elif idade <= 19:
    print('Atleta {}JUNIOR.{}'.format(forms['amarelo'], forms['limpa']))
elif idade == 20:
    print('Atleta {}SÊNIOR.{}'.format(forms['amarelo'], forms['limpa']))
else:
    print('Atleta {}MASTER.{}'.format(forms['amarelo'], forms['limpa']))