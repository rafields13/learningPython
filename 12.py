# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

x = float(input('Digite o preço do produto aqui, por favor: '))
dis = x - (x * (5 / 100))
print(f'O valor do produto com preço de {x} reais com 5% de desconto fica {dis:.2f} reais.')
