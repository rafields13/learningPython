# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

x = float(input('Digite aqui o valor em metros, por favor: '))
cm = x * 100
mm = x * 1000
print(f'O valor {x}, dado em metros, convertido em centímetros é {cm:.2f} e convertido em milímetros é: {mm:.2f}.')
