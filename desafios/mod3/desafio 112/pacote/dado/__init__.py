from pacote import cores

def LeiaDinheiro():
    preço = str(input(f'>>> Digite o preço: {cores.Azul()}R$'))

    float(preço[:])

    if preço.strip() == '' or preço:
        print(f'{cores.Vermelho()}[ERRO]: "" é um preço inválido!{cores.Padrão()}')

    if preço.find('.') > 0:
        preço.replace('.', ',')

    return preço