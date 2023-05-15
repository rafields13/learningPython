# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um
# programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
w = input('Digite o nome do primeiro aluno, por favor: ')
x = input('Digite o nome do segundo aluno, por favor: ')
y = input('Digite o nome do terceiro aluno, por favor: ')
z = input('Digite o nome do quarto aluno, por favor: ')
stu = [w, x, y, z]
shuffle(stu)
print(f'A ordem de apresentação é {stu}.')
