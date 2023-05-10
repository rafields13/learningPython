# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele.

x = input('Digite algo, por favor: ')
print(type(x))
print(x.isalnum())
print(x.isalpha())
print(x.isascii())
print(x.isdigit())
print(x.islower())
print(x.isdecimal())
print(x.isidentifier())
print(x.isnumeric())
print(x.isprintable())
print(x.isspace())
print(x.istitle())
print(x.isupper())
