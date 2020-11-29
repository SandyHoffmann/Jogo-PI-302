import pygame
import os

def load_image(name):
    image = pygame.image.load(name)
    return image

class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        super(Personagem, self).__init__()

        self.imagem_maga = []
        self.imagem_maga.append(load_image('imagens/personagens/maga/000.png'))
        self.imagem_maga.append(load_image('imagens/personagens/maga/001.png'))
        self.imagem_maga.append(load_image('imagens/personagens/maga/002.png'))
        self.imagem_maga.append(load_image('imagens/personagens/maga/003.png'))
        self.imagem_maga.append(load_image('imagens/personagens/maga/004.png'))
        self.imagem_maga.append(load_image('imagens/personagens/maga/005.png'))
        self.imagem_maga.append(load_image('imagens/personagens/maga/006.png'))
        self.imagem_maga.append(load_image('imagens/personagens/maga/007.png'))
        self.imagem_maga.append(load_image('imagens/personagens/maga/008.png'))
        self.imagem_maga.append(load_image('imagens/personagens/maga/009.png'))
        self.menubg=[]
        self.menubg.append(load_image('imagens/bg1.png'))
        self.menubg.append(load_image('imagens/bg2.png'))
        self.index = 0
        self.menu= self.menubg
        self.image = self.imagem_maga[self.index]
        self.logo=[]
        self.logo.append(load_image('imagens/logo1.png'))
        self.logo.append(load_image('imagens/logo2.png'))
        self.logoanimado=self.logo
    def update(self):
        '''This method iterates through the elements inside self.images and 
        displays the next one each tick. For a slower animation, you may want to 
        consider using a timer of some sort so it updates slower.'''
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        if self.index >= len(self.menu):
            self.index = 0
        self.menu = self.menu[self.index]

    def main(self):
        pygame.init()
        return self.imagem_maga,self.menu,self.logo
    def logo(self):
        pygame.init()
        return self.logo
    def menu(self):
        pygame.init()
        return self.menu
