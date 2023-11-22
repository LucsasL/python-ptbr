from pacote import cores

# Funções externas
def moeda(num, form = False, moeda = 'R$'):
    if form:
        return f'{cores.Azul()}{moeda}{num:.2f}{cores.Padrão()}'.replace(',', '.')
        
    else:
        return num

def Aumentar(num, aum, form = False, moeda = 'R$'):
    num += (num * aum / 100)
    if form:
        return f'{cores.Azul()}{moeda}{num:.2f}{cores.Padrão()}'.replace('.', ',')
        
    else:
        return num

def Diminuir(num, dim, form = False, moeda = 'R$'):
    num -= (num * dim / 100)
    if form:
        return f'{cores.Azul()}{moeda}{num:.2f}{cores.Padrão()}'.replace('.', ',')
        
    else:
        return num

def Metade(num, form = False, moeda = 'R$'):
    num /= 2
    if form:
        return f'{cores.Azul()}{moeda}{num:.2f}{cores.Padrão()}'.replace('.', ',')
        
    else:
        return num

def Dobro(num, form = False, moeda = 'R$'):
    num *= 2
    if form:
        return f'{cores.Azul()}{moeda}{num:.2f}{cores.Padrão()}'.replace('.', ',')
        
    else:
        return num