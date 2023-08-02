Content = input('Digite algo: ')

print('O tipo primitivo desse calor é ', type(Content))

print('Só tem espaços? ', Content.isspace())

print('É um número? ', Content.isnumeric())

print('É alfabético? ', Content.isalpha())

print('É alfanumérico? ', Content.isalnum())

print('Está em maiúscula? ', Content.isupper())

print('Está em minúsculas? ', Content.islower())

print('Está capitalizada? ', Content.istitle())