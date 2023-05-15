# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

x = float(input('Digite aqui a primeira nota, por favor: '))
y = float(input('Digite aqui a segunda nota, por favor: '))
ave = (x + y) / 2
print(f'A média das notas {x} e {y} é {ave:.2f}.')
