# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido.

from random import choice
w = input('Digite o nome do primeiro aluno, por favor: ')
x = input('Digite o nome do segundo aluno, por favor: ')
y = input('Digite o nome do terceiro aluno, por favor: ')
z = input('Digite o nome do quarto aluno, por favor: ')
stu = [w, x, y, z]
chS = choice(stu)
print(f'O aluno escolhido foi o (a) {chS}.')
