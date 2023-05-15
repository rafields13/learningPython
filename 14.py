# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

x = float(input('Digite a temperatura em ºC, por favor: '))
fah = x * 1.8 + 32
print(f'A temperatura {x} ºC convertida para fahrenheit fica {fah} ºF.')
