maismil = total = barato = cont = 0

while True:
    nomeP = str(input('>>> Digite o nome o produto: '))

    preço = float(input('>>> Digite o preço do produto: R$'))

    resp = str(input('>>> Adicionar mais produtos? [S / N]: ')).upper().strip()

    total += preço

    if cont == 0:
        barato = preço
        Pbar = nomeP

    if barato > preço:
        Pbar = nomeP
        barato = preço

    if preço > 1000:
        maismil += 1

    cont += 1

    if resp != 'S':
        while resp not in 'SN':
            resp = str(input('>>> Opção inválida! Digite novamente [S / N]: ')).upper()[0].strip()

            if resp == 'N':
                break
    
    if resp == 'N':
        break

print(f'\n... O total gasto na compra será R${total:.2f}.')

print(f'\n... Dos produtos digitados, {maismil} custam mais que R$1000,00.')

print(f'\n... O produto mais barato foi o {Pbar}, custando apenas R${barato:.2f}.')