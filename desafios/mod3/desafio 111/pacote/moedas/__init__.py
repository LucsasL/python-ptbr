from pacote import cores

# Funções externas
def Resumo(p, aum, dim):
    print(f'{cores.Roxo()}-={cores.Padrão()}' * 30)
    print(f'RESUMO DO VALOR'.center(60))
    print(f'{cores.Roxo()}-{cores.Padrão()}' * 60)
    print(f'{"Preço analisado:":<50}{f"R$ {p:.2f}":>5}')
    print(f'{"Dobro do preço:":<50}{f"R$ {p * 2:.2f}":>5}')
    print(f'{"Metade do preço":<50}{f"R$ {p / 2:.2f}":>5}')
    print(f'{f"{aum}% de aumento:":<50}{f"R$ {p + (p * aum / 100):.2f}":>5}')
    print(f'{f"{dim}% de redução:":<50}{f"R$ {p - (p * dim / 100):.2f}":>5}')
    print(f'{cores.Roxo()}-={cores.Padrão()}' * 30)