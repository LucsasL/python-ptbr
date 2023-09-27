from time import sleep

forms = {'limpa': '\033[m',
         'bold': '\033[1m',
         'roxo': '\033[1;35m'}

print('{}-=-{}'.format(forms['roxo'], forms['limpa']) * 20)
print('{}{:^55}{}'.format(forms['bold'], 'ANALISADOR DE VALORES', forms['limpa']))
print('{}-=-{}'.format(forms['roxo'], forms['limpa']) * 20)

n1 = float(input('>>> Digite um número: '))

n2 = float(input('>>> Digite outro número: '))

escolha = 0

analise = 1

while escolha != 5:
    if analise > 1:
        sleep(2)

    print('\n-------------------')
    print('[1] {:20}'.format('Somar'))
    print('[2] {:20}'.format('Multiplicar  '))
    print('[3] {:20}'.format('Mostrar Maior'))
    print('[4] {:20}'.format('Novos Números'))
    print('[5] {:20}'.format('Sair do programa '))

    escolha = int(input('\n>>> Selecione analise: '))

    if escolha == 1:
        s = n1 + n2
        print('\n... A soma entre {:.2f} e {:.2f} é igual a {:.2f}.'.format(n1, n2, s))

    elif escolha == 2:
        mult = n1 * n2
        print('\n... A multiplicação entre {:.2f} e {:.2f} é {:.2f}.'.format(n1, n2, mult))

    elif escolha == 3:
        if n1 > n2:
            print('\n... O maior número é o primeiro: {:.2f}'.format(n1))

        elif n2 > n1:
            print('\n... O maior número é o segundo: {:.2f}'.format(n2))

        else:
            print('\n... Os dois números são iguais.')

    elif escolha == 4:
        n1 = float(input('>>> Digite um número: '))

        n2 = float(input('>>> Digite outro número: '))

    elif escolha != 5:
        escolha = int(input('>>> Valor inválido! Digite novamente: '))

    analise += 1

print('... Programa finalizado.')