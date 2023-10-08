produtos = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.9,
            'Estojo', 25,
            'Transferidor', 4.2,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.3,
            'Livro', 34.9)

print('-' * 55)
print('LISTAGEM DE PREÇO'.center(55))
print('-' * 55)
for n in range(0, len(produtos)):
    if n % 2 == 0:
        print(f'{produtos[n]:.<45}', end='')
    else:
        print(f' R$ {produtos[n]:>5.2f}')
print('-' * 55)