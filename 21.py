# Faça um programa que abra e reproduza o áudio de um arquivo MP3.

from pygame import mixer, event
pygame.init()
mixer.music.load('arquivoMp3Qualquer')
mixer.music.play()
event.wait

# Ao fazer o download do arquivo MP3, coloque-o na mesma pasta do arquivo do exercício!
