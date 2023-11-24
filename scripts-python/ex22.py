forms = {
    'padrão': '\033[m',
    'bold': '\033[1m',
    'roxo': '\033[1;35m'
}

def Titulo(msg):
    print(f'{forms["roxo"]}-={forms["padrão"]}' * 45)
    print(f'{forms["bold"]}{msg}'.center(90))
    print(f'{forms["roxo"]}-={forms["padrão"]}' * 45)

# Programa Principal
Titulo('ERROS E EXCEÇÕES')

try:
    a = int(input(f'{forms["bold"]}... Numerador: {forms["padrão"]}'))
    b = int(input(f'{forms["bold"]}... Denominador: {forms["padrão"]}'))
    r = a / b

except (ValueError, TypeError):
    print(f'... Houveram problemas com os tipos de dados adicionados ao campos de digitação.')

except ZeroDivisionError:
    print(f'... Não é possível dividir um número por 0.')

except KeyboardInterrupt:
    print(f'... Não foram adicionados dados.')

else:
    print(f'... O resultado é igual a {r:.2f}.')

finally:
    print(f'... Volte sempre! :)')