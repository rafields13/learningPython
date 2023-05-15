# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

x = int(input('Digite um número, por favor: '))
dou = x * 2
tri = x * 3
sqR = x ** (1 / 2)
print(f'O dobro de {x} é {dou}, o triplo é {tri} e a raiz quadrada é {sqR:.2f}.')
