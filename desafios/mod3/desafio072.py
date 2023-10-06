números = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

dig = int(input('>>> Digite um número entre 0 e 20: '))

if dig <= 20 and dig >= 0:
    print(f'O número digitado foi {números[dig]}.')
else:
    while True:
        dig = int(input('>>> Número inválido! Digite um número entre 0 e 20: '))

        if dig <= 20 and dig >= 0:
            print(f'O número digitado foi {números[dig]}.')
            break