números = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

resp = ' '

while resp != 'N':
    dig = int(input('>>> Digite um número entre 0 e 20: '))

    if 0 <= dig <= 20:
        print(f'... O número digitado foi {números[dig]}.')

        resp = str(input('>>> Quer digitar mais um número [S / N]: ')).strip().upper()[0]

        if resp != 'S' and resp != 'N':
            while True:
                resp = str(input('>>> Opção inválida! Digite novamente [S / N]: ')).strip().upper()[0]
                
                if resp == 'N' or resp == 'S':
                    break
        
        elif resp == 'N':
            break
                    
    else:
        while True:
            dig = int(input('>>> Número inválido! Digite um número entre 0 e 20: '))

            if 0 <= dig <= 20:
                print(f'... O número digitado foi {números[dig]}.')

                resp = str(input('>>> Quer digitar mais um número [S / N]: ')).strip().upper()[0]

                if resp != 'S' and resp != 'N':
                    while True:
                        resp = str(input('>>> Opção inválida! Digite novamente [S / N]: ')).strip().upper()[0]
                        
                        if resp == 'N' or resp == 'S':
                            break