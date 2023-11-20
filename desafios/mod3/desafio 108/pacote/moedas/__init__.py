from pacote import cores

# Funções externas
def moeda(num):
    return f'{cores.Azul()}R${num:.2f}{cores.Padrão()}'

def Aumentar(num, aum):
    num += (num * aum / 100)
    return f'{cores.Azul()}R${num:.2f}{cores.Padrão()}'

def Diminuir(num, dim):
    num -= (num * dim / 100)
    return f'{cores.Azul()}R${num:.2f}{cores.Padrão()}'

def Metade(num):
    num /= 2
    return f'{cores.Azul()}R${num:.2f}{cores.Padrão()}'

def Dobro(num):
    num *= 2
    return f'{cores.Azul()}R${num:.2f}{cores.Padrão()}'