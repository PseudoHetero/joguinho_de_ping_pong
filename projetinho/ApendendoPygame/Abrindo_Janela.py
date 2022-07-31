import pygame.display
from Input_Teclas import teclas


# inicia o pygame
pygame.init()
# open a janela (sem loop)
display = pygame.display.set_mode([840, 480])


# Função do visual da janela
def visual():
    # Usado para mudar o fundo da janela, numeros sao de acordo com o esquema de cor RDB
    display.fill([49, 146, 163])
    # Comando para mudar o nome da janela
    pygame.display.set_caption("Ferdinando")


# Game loop - loop para manter o game rodando ate algo acontecer
gameLoop = True
while gameLoop:
    teclas()
    visual()
    pygame.display.update()
