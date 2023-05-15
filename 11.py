# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

wid = float(input('Digite a largura da parede aqui, por favor: '))
hei = float(input('Digite a altura da parede aqui, por favor: '))
are = wid * hei
amI = are / 2
print(f'A área é {are} m² e a quantidade de tinta necessária para pintá-la é {amI} litros.')
