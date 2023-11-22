from pacote import cores

def LeiaDinheiro():
    while True:
        preço = str(input(f'>>> Digite o preço: {cores.Azul()}R$')).strip().replace(',', '.')

        if preço.strip() == '' or preço.isalpha():
            print(f'{cores.Vermelho()}... [ERRO]: "{preço}" é um preço inválido!{cores.Padrão()}')

        else:
            break

    return float(preço)