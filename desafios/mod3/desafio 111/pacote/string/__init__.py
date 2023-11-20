from pacote import cores

def Titulo(title):
    print(f'{cores.Roxo()}-={cores.Padrão()}' * 30)
    print(f'{cores.Bold()}{title}{cores.Padrão()}'.center(60))
    print(f'{cores.Roxo()}-={cores.Padrão()}' * 30)