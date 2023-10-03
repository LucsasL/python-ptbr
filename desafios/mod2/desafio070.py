maismil = total = barato = cont = 0

print('-' * 45)
print('{:^45}'.format('COMPRAS NO HIPERMECADO'))
print('-' * 45)

while True:
    nomeP = str(input('>>> Digite o nome o produto: '))

    preço = float(input('>>> Digite o preço do produto: R$'))

    resp = str(input('>>> Adicionar mais produtos? [S / N]: ')).strip().upper()

    total += preço

    if cont == 0 or barato > preço:
        barato = preço
        Pbar = nomeP

    if preço > 1000:
        maismil += 1

    cont += 1

    if resp != 'S':
        while resp not in 'SN':
            resp = str(input('>>> Opção inválida! Digite novamente [S / N]: ')).strip().upper()[0]

            if resp == 'N':
                break
    
    if resp == 'N':
        break

print('{:-^45}'.format(' FIM DO PROGRAMA '))

print(f'\n... O total gasto na compra será R${total:.2f}.')

print(f'\n... Dos produtos digitados, {maismil} custam mais que R$1000,00.')

print(f'\n... O produto mais barato foi o {Pbar}, custando apenas R${barato:.2f}.')