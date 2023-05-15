# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira.

from math import trunc
x = float(input('Digite um número, por favor: '))
print(f'A parte inteira de {x} é {trunc(x)}.')

# Pode ser feito de forma mais simples:

x = float(input('Digite um número, por favor: '))
print(f'A parte inteira de {x} é {int(x)}.')
