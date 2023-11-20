# Funções externas
def Fatorial(n):
    for c in range(n - 1, 1, -1):
        n *= c
    return n

def Dobro(n):
    return n * 2

def Triplo(n):
    return n * 3