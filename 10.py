# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.

x = float(input('Digite a quantidade de dinheiro que quer fazer a equivlência para Dólar, por favor: '))
dol = x / 4.92
print(f'{x} reais equivalem a {dol:.2f} dólares.')
