# Escreva um programa que pergunte a quantidade de kilômetros percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,
# 15 por kilômetro rodado.

x = float(input('Digite aqui a quantidade de kilômetros percorridos, por favor: '))
y = int(input('Digite aqui a quantidade de dias que ele foi alugado, por favor: '))
pri = x * 0.15 + y * 60
print(f'O preço total a se pagar é de {pri} reais.')
