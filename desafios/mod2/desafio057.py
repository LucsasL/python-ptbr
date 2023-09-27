sexo = str(input('>>> Digite o sexo [M / F]: ')).upper()[0].strip()

while sexo not in 'MmFf':
    sexo = str(input('... Sexo inválido! Digite novamente [M / F]: '))
    
print('... Sexo {} registrado com sucesso'.format(sexo))