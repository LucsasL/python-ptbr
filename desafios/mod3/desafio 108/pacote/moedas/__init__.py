from pacote import cores

# Funções externas
def moeda(num, moeda = 'R$'):
    return f'{cores.Azul()}{moeda}{num:.2f}{cores.Padrão()}'.replace('.', ',')

def Aumentar(num = 0, aum = 0, moeda = 'R$'):
    num += (num * aum / 100)
    return f'{cores.Azul()}{moeda}{num:.2f}{cores.Padrão()}'.replace('.', ',')

def Diminuir(num = 0, dim = 0, moeda = 'R$'):
    num -= (num * dim / 100)
    return f'{cores.Azul()}{moeda}{num:.2f}{cores.Padrão()}'.replace('.', ',')

def Metade(num = 0, moeda = 'R$'):
    num /= 2
    return f'{cores.Azul()}{moeda}{num:.2f}{cores.Padrão()}'.replace('.', ',')

def Dobro(num = 0, moeda = 'R$'):
    num *= 2
    return f'{cores.Azul()}{moeda}{num:.2f}{cores.Padrão()}'.replace('.', ',')