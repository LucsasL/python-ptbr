print('=' * 30)
print('ANALISE DE DADOS')
print('=' * 30)

pmaior = nump = h = mm20 = 0

while True:
    nump += 1

    print(f'{nump}° PESSOA')
    print('-' * 30)

    # Formulário de pergunta
    idade = int(input('>>> Digite a idade: '))

    sexo = str(input('>>> Digite o sexo [M / F]: ')).upper()[0].strip()

    resp = str(input('>>> Adicionar mais pessoas? [S / N]: ')).upper()[0].strip()
    
    # Calcula parâmetros
    if idade > 18:
        pmaior += 1

    if idade < 20 and sexo == 'F':
        mm20 += 1

    if sexo == 'M':
        h += 1

    # Testa possibilidade de erro ao digitar
    if resp != 'S':
        if resp == 'N':
            break

        while resp not in 'SN':
            resp = str(input('>>> Opção inválida! Digite novamente [S / N]: ')).upper()[0].strip()

            if resp == 'N':
                break
    
    if resp == 'N':
        break

print('''\n... Dos dados digitados, podemos concluir que {} pesssoas tem mais de 18 anos, {} pessoas são homens e {} das mulheres digitadas tem menos de 20 anos.'''.format(pmaior, h, mm20))