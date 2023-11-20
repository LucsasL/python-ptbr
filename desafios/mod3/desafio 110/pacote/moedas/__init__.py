from pacote import cores

# Funções externas
def Resumo(p, aum, dim):
    print(f'{cores.Roxo()}-={cores.Padrão()}' * 30)
    print(f'RESUMO DO VALOR'.center(60))
    print(f'{cores.Roxo()}-{cores.Padrão()}' * 60)
    print(f'{"Preço analisado:":<50}{f"R$ {p:.2f}":>5}')
    print(f'{"Dobro do preço:":<50}{f"R$ {p * 2:.2f}":>5}')
    print(f'{"Metade do preço":<50}{f"R$ {p / 2:.2f}":>5}')
    print(f'{f"{aum}% de aumento:":<50}{f"R$ {p + (p * aum / 100)}":>5.2f}')
    print(f'{f"{dim}% de redução:":<50}{f"R$ {p - (p * dim / 100)}":>5.2f}')
    print(f'{cores.Roxo()}-={cores.Padrão()}' * 30)

def moeda(num):
    return f'{cores.Azul()}R${num:.2f}{cores.Padrão()}'

def Aumentar(num, aum, form = False):
    num += (num * aum / 100)
    if form:
        return f'{cores.Azul()}R${num:.2f}{cores.Padrão()}'
        
    else:
        return num

def Diminuir(num, dim, form = False):
    num -= (num * dim / 100)
    if form:
        return f'{cores.Azul()}R${num:.2f}{cores.Padrão()}'
        
    else:
        return num

def Metade(num, form = False):
    num /= 2
    if form:
        return f'{cores.Azul()}R${num:.2f}{cores.Padrão()}'
        
    else:
        return num

def Dobro(num, form = False):
    num *= 2
    if form:
        return f'{cores.Azul()}R${num:.2f}{cores.Padrão()}'
        
    else:
        return num