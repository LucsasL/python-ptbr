cont = s = 0

while True:
    num = int(input(f'>>> Digite o {cont + 1}° número [999 para parar]: '))
    if num == 999:
        break
    cont += 1
    s += num

print(f'\n... Foram digitados {cont} números durante a execução do programa. A soma de todos eles foi {s}.')