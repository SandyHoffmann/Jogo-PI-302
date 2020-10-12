import pygame
import os
pygame.init()
font = pygame.font.Font(os.path.join('fontes/ka1.ttf'), 30)

class Historia(pygame.sprite.Sprite):
    def __init__(self,ponto_de_parada,sucesso,falha):
        self.ponto_de_parada=ponto_de_parada
        self.sucesso=sucesso
        self.falha=falha

    def historia(self,ponto_de_parada,win):
        if ponto_de_parada==1:
            texto=font.render(str("Ola bartender"), True, (255, 255, 255))
            win.blit(texto,(800,100))