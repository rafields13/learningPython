# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
x = float(input('Digite aqui o valor do ângulo, por favor: '))
radX = radians(x)
print(f'O valor do seno de {x} é {sin(radX):.2f}, o cosseno é {cos(radX):.2f} e a tangente é {tan(radX):.2f}.')
