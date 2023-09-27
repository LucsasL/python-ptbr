sexo = 'Indefinido'

while sexo != 'M' or 'F':
    sexo = str(input('>>> Digite o sexo [M / F]: ')).upper().strip()
    if sexo != 'M' or 'F':
        print('... Sexo inválido! Digite novamente!')
print('Acabou')