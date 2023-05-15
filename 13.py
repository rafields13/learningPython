# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

x = float(input('Digite o salário atual aqui, por favor: '))
inc = x + (x * (15 / 100))
print(f'O novo salário é de {inc:.2f} reais.')
