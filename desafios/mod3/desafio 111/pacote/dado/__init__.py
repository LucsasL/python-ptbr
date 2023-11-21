from pacote import cores

# Funções externas
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