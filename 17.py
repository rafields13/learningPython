# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

from math import pow, sqrt
x = float(input('Digite aqui o comprimento do cateto oposto, por favor: '))
y = float(input('Digite aqui o comprimento do cateto adjacente, por favor: '))
hip = sqrt(pow(x, 2) + pow(y, 2))
print(f'A hipotenusa desse triângulo mede {hip:.2f}.')

# Pode ser feito de forma mais simples:

x = float(input('Digite aqui o comprimento do cateto oposto, por favor: '))
y = float(input('Digite aqui o comprimento do cateto adjacente, por favor: '))
hip = (x ** 2 + y ** 2) ** (1 / 2)
print(f'A hipotenusa desse triângulo mede {hip:.2f}.')

# Pode ser feito de forma mais simples ainda:

from math import hypot
x = float(input('Digite aqui o comprimento do cateto oposto, por favor: '))
y = float(input('Digite aqui o comprimento do cateto adjacente, por favor: '))
hip = hypot(x, y)
print(f'A hipotenusa desse triângulo mede {hip:.2f}.')
