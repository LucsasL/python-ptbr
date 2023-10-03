maismil = total = barato = cont = 0

resp = '...'

while True:
    if resp == 'N':
        break

    nomeP = str(input('>>> Digite o nome o produto: '))

    preço = float(input('>>> Digite o preço do produto: R$'))

    resp = str(input('>>> Adicionar mais produtos? [S / N]: ')).upper().strip()

    total += preço

    if cont == 0:
        barato = preço

    if barato > preço:
        Pbar = nomeP
        barato = preço

    if preço > 1000:
        maismil += 1

    cont += 1

    if resp == 'N':
        break
    elif resp != 'S':
        while True:
            resp = str(input('>>> Opção inválida! Digite novamente [S / N]: ')).upper().strip()

            if resp == 'N' or 'S':
                break

print(f'\n... O total gasto na compra será R${total:.2f}.')

print(f'\n... Dos produtos digitados, {maismil} custam mais que R$1000,00.')

print(f'\n... O produto mais barato foi o {Pbar}, custando apenas R${barato:.2f}.')