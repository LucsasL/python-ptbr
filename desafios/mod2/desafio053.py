frase = str(input('Digite uma frase: ')).upper().strip()

palavras = frase.split()

junto = ''.join(palavras)

inv = ''

for letra in range(len(junto) - 1, -1, -1):
    inv += junto[letra]

print('A frase digitada: {} invertida é {}.'.format(frase, inv))

if inv == junto:
    print('A frase digitada é um Palíndromo!')
else:
    print('A frase digitada não é um Palíndromo.')