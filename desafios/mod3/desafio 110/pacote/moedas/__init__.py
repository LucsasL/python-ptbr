from pacote import cores

# Funções externas
def formMoeda(p, form = True, moeda = 'R$'):
    res = f'{moeda} {p:.2f}'.replace('.', ',')
    return res if form is True else p

def Resumo(p, aum, dim, form = True):
    print(f'{cores.Roxo()}-={cores.Padrão()}' * 30)
    print(f'RESUMO DO VALOR'.center(60))
    print(f'{cores.Roxo()}-{cores.Padrão()}' * 60)
    print(f'{"Preço analisado:":<43}\t{formMoeda(p)}')
    print(f'{"Dobro do preço:":<43}\t{formMoeda(p * 2)}')
    print(f'{"Metade do preço":<43}\t{formMoeda(p / 2)}')
    print(f'{f"{aum}% de aumento:":<43}\t{formMoeda(p + (p * aum / 100))}')
    print(f'{f"{dim}% de redução:":<43}\t{formMoeda(p - (p * dim / 100))}')
    print(f'{cores.Roxo()}-={cores.Padrão()}' * 30)