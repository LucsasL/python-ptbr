sexo = 'Indefinido'

while sexo not in 'MmFf':
    sexo = str(input('>>> Digite o sexo [M / F]: ')).upper()[0].strip()
    if sexo not in 'MmFf':
        print('... Sexo inválido! Digite novamente!')
print('Sexo {} registrado com sucesso'.format(sexo))