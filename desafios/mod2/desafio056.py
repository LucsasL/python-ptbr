for c in range(1, 5):
    nome = str(input('>>> Digite o nome da {}° pessoa: '.format(c)))
    idade = int(input('>>> Digite a idade da {}° pessoa: '.format(c)))
    sexo = str(input('>>> Digite o sexo da {}° pessoa [M / F]: '.format(c)).upper())

    print('... PESSOA {}: {}, {}, {}'.format(c, nome, idade, sexo))