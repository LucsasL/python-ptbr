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

    sexo = str(input('>>> Digite o sexo [M / F]: ')).strip().upper()[0]

    if sexo == 'M':
        h += 1

    # Testa possibilidade de erro ao digitar no input de sexo
    elif sexo != 'F':
        while sexo not in 'MF':
            sexo = str(input('>>> Opção inválida! Digite novamente [M / F]: ')).strip().upper()[0]

            if sexo == 'M':
                h += 1

    resp = str(input('>>> Adicionar mais pessoas? [S / N]: ')).strip().upper()[0]
    
    # Calcula parâmetros
    if idade > 18:
        pmaior += 1

    if idade < 20 and sexo == 'F':
        mm20 += 1

    # Testa possibilidade de erro ao digitar no input de adição
    if resp != 'S':
        if resp == 'N':
            break

        while resp not in 'SN':
            resp = str(input('>>> Opção inválida! Digite novamente [S / N]: ')).strip().upper()[0]

            if resp == 'N':
                break
    
    if resp == 'N':
        break

print(f'\n... Dos dados digitados, podemos concluir que {pmaior} pesssoas tem mais de 18 anos.')

print(f'\n... {h} das pessoas são homens.')

print(f'\n... E {mm20} das mulheres digitadas tem menos de 20 anos.')