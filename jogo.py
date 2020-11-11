import pygame
from historia import Historia
import textboxify
from personagem import Personagem
from parametros import Grupo_Parametros

pygame.init()
ALTURA=1200
LARGURA=800
background = pygame.image.load("imagens/background.png")
salty=pygame.image.load("imagens/salty.png")
candy=pygame.image.load("imagens/candy.png")
hot=pygame.image.load("imagens/hot.png")
tasty=pygame.image.load("imagens/tasty.png")
sour=pygame.image.load("imagens/sour.png")
quadrado_quant=pygame.image.load("imagens/quadrado2.png")
tamanhos=[[60,80],[50,70],[40,55],[25,70],[40,50]]
tamanhos_quad=[[10,160],[10,265],[10,370],[10,475],[10,580]]
reset=pygame.image.load("imagens/reset.png")
mandar=pygame.image.load("imagens/mandar.png")
white = (255, 255, 255) 
font = pygame.font.SysFont(None, 40)
display_surface = pygame.display.set_mode((ALTURA, LARGURA )) 
b = pygame.mixer.Sound("sons/sound0.ogg")
a = pygame.mixer.Sound("sons/sound.ogg")
tela_sea=pygame.image.load("imagens/seawater.png")
tela_heavy=pygame.image.load("imagens/heavydrink.png")
tela_sugar=pygame.image.load("imagens/sugarrush.png")
tela_nao_deu=pygame.image.load("imagens/naodeucerto.png")
tela_falas=pygame.image.load("imagens/quadradofalas.png")
mouse = pygame.mouse.get_pressed()


class Jogo(object):

    def __init__(self,ALTURA,LARGURA):
        self.altura=ALTURA
        self.largura=LARGURA
        self.tela_certa=0
        self.tela_errada=False
        self.bebida_1=0
        self.bebida_2=0
        self.bebida_3=0
        self.bebida_4=0
        self.bebida_5=0
        self.mistura=[]
        self.diferenca = [0,0]
        self.primeiro = True
        self.carregando = False
        self.musica_bebida=5
        self.lista_lugares=[[480,280],[540,292],[590,300],[635,290],[665,310]]
        self.ponto_de_parada=0
        self.tempo=0
        self.tempo_dialogo=0
        self.relogio=1
        self.texto_anterior="-"
        self.botao_pressionado = False
        self.frameinit=0
        self.classe_parametros = Grupo_Parametros(0,0,0)

    def main(self):
        display_surface = pygame.display.set_mode((self.altura, self.largura)) 
        self.win=pygame.display.set_mode((self.altura,self.largura))
        pygame.display.set_caption("alo")
        self.update()
    
    def update(self):
        while True:
            mouse = pygame.mouse.get_pressed()
            mousepos=pygame.mouse.get_pos()
            for event in pygame.event.get() : 
                if event.type == pygame.QUIT : 
                    pygame.quit() 
                    quit()  
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.botao_pressionado = True
                    
                elif event.type != pygame.MOUSEBUTTONDOWN:        
                    self.botao_pressionado = False

                if mousepos[0]>10 and mousepos[0]<10+100 and self.botao_pressionado == True:
                    if mousepos[1]>30 and mousepos[1]<30+50:
                        if self.bebida_1>((self.bebida_1+self.bebida_2+self.bebida_3+self.bebida_4+self.bebida_5)*0.6): 
                            print("Sea Water")
                            self.bebida_1=0
                            self.bebida_2=0
                            self.bebida_3=0
                            self.bebida_4=0
                            self.bebida_5=0
                            self.tela_certa=1
                            self.ponto_de_parada=1
                            self.classe_parametros.set_clerigo(2)
                            self.classe_parametros.get_clerigo()
                            print(str(self.classe_parametros.get_clerigo()))
                        elif self.bebida_3>((self.bebida_1+self.bebida_2+self.bebida_3+self.bebida_4+self.bebida_5)*0.2) and self.bebida_4>((self.bebida_1+self.bebida_2+self.bebida_3+self.bebida_4+self.bebida_5)*0.2): 
                            print("Heavy Drink")
                            self.bebida_1=0
                            self.bebida_2=0
                            self.bebida_3=0
                            self.bebida_4=0
                            self.bebida_5=0
                            self.tela_certa=2
                        elif self.bebida_2>((self.bebida_1+self.bebida_2+self.bebida_3+self.bebida_4+self.bebida_5)*0.8): 
                            print("Sugar Rush")
                            self.bebida_1=0
                            self.bebida_2=0
                            self.bebida_3=0
                            self.bebida_4=0
                            self.bebida_5=0
                            self.tela_certa=3
                        else:
                            print("Nada deu certo")
                            self.bebida_1=0
                            self.bebida_2=0
                            self.bebida_3=0
                            self.bebida_4=0
                            self.bebida_5=0
                            self.tela_certa=4
                    
                    if mousepos[0]>10 and mousepos[0]<10+100 and self.botao_pressionado == True:
                        if mousepos[1]>90 and mousepos[1]<90+50:
                            self.bebida_1=0
                            self.bebida_2=0
                            self.bebida_3=0
                            self.bebida_4=0
                            self.bebida_5=0
            pygame.display.update()  

            if mouse == (1,0,0):
                for x in range(5):
                    if mousepos[0]>self.lista_lugares[x][0] and mousepos[0]<self.lista_lugares[x][0]+tamanhos[x][0]:
                        if mousepos[1]>self.lista_lugares[x][1] and mousepos[1]<self.lista_lugares[x][1]+tamanhos[x][1]:
                            if self.primeiro == True:
                                self.diferenca = [mousepos[0]-self.lista_lugares[x][0],mousepos[1]-self.lista_lugares[x][1]]
                                self.primeiro = False
                                self.musica_bebida=x
                            self.carregando = True
            else:
                if self.primeiro == False:
                    self.lista_lugares = [[480,280],[540,292],[590,300],[635,290],[665,310]]
                    if (mousepos[0]>458 and mousepos[0]<564) and (mousepos[1]>410 and mousepos[1]<546):
                        if self.musica_bebida == 0 and self.mistura.count(0)<9:
                            pygame.mixer.Sound.play(a)
                            self.bebida_1+=1
                        elif self.musica_bebida == 1 and self.mistura.count(1)<9:
                            pygame.mixer.Sound.play(b)
                            self.bebida_2+=1
                        elif self.musica_bebida == 2 and self.mistura.count(2)<9:
                            pygame.mixer.Sound.play(b)
                            self.bebida_3+=1
                        elif self.musica_bebida == 3 and self.mistura.count(3)<9:
                            pygame.mixer.Sound.play(b)
                            self.bebida_4+=1
                        elif self.musica_bebida == 4 and self.mistura.count(4)<9:
                            pygame.mixer.Sound.play(b)
                            self.bebida_5+=1

                self.primeiro = True
                self.carregando = False
        

            if self.carregando == True:
                    self.lista_lugares[self.musica_bebida][0]=mousepos[0]-self.diferenca[0]
                    self.lista_lugares[self.musica_bebida][1]=mousepos[1]-self.diferenca[1]
    
            self.draw()

    def draw(self):
        self.win.fill((20,20,180))
        self.win.blit(background,(0,0))
        self.win.blit(quadrado_quant,(tamanhos_quad[0]))
        self.win.blit(quadrado_quant,(tamanhos_quad[1]))
        self.win.blit(quadrado_quant,(tamanhos_quad[2]))
        self.win.blit(quadrado_quant,(tamanhos_quad[3]))
        self.win.blit(quadrado_quant,(tamanhos_quad[4]))
        self.win.blit(mandar,(10,30))
        self.win.blit(reset,(10,90))
        self.win.blit(salty,(self.lista_lugares[0]))
        self.win.blit(candy,(self.lista_lugares[1]))
        self.win.blit(sour,(self.lista_lugares[2]))
        self.win.blit(hot,(self.lista_lugares[3]))
        self.win.blit(tasty,(self.lista_lugares[4]))
        text=font.render(str(self.bebida_1), True, (255, 255, 255))
        self.win.blit(text,(tamanhos_quad[0][0]+75,tamanhos_quad[0][1]+70))

        text2=font.render(str(self.bebida_2), True, (255, 255, 255))
        self.win.blit(text2,(tamanhos_quad[1][0]+75,tamanhos_quad[1][1]+70))

        text3=font.render(str(self.bebida_3), True, (255, 255, 255))
        self.win.blit(text3,(tamanhos_quad[2][0]+75,tamanhos_quad[2][1]+70))

        text4=font.render(str(self.bebida_4), True, (255, 255, 255))
        self.win.blit(text4,(tamanhos_quad[3][0]+75,tamanhos_quad[3][1]+70))

        text5=font.render(str(self.bebida_5), True, (255, 255, 255))
        self.win.blit(text5,(tamanhos_quad[4][0]+75,tamanhos_quad[4][1]+70))

        if self.tela_certa!=0:
            if self.tela_certa==1:
                self.win.blit(tela_sea,(LARGURA//2-100,ALTURA//2-300))
            if self.tela_certa==2:
                self.win.blit(tela_heavy,(LARGURA//2-100,ALTURA//2-300))
            if self.tela_certa==3:
                self.win.blit(tela_sugar,(LARGURA//2-100,ALTURA//2-300))
            if self.tela_certa==4:
                self.win.blit(tela_nao_deu,(LARGURA//2-100,ALTURA//2-300))
            for event in pygame.event.get() : 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.tela_certa=0
                    


        self.win.blit(salty,(tamanhos_quad[0][0]+20,tamanhos_quad[0][1]+10))
        self.win.blit(candy,(tamanhos_quad[1][0]+20,tamanhos_quad[1][1]+10))
        self.win.blit(sour,(tamanhos_quad[2][0]+25,tamanhos_quad[2][1]+20))
        self.win.blit(hot,(tamanhos_quad[3][0]+40,tamanhos_quad[3][1]+10))
        self.win.blit(tasty,(tamanhos_quad[4][0]+25,tamanhos_quad[4][1]+20))
        classepersonagem= Personagem()
        maga = classepersonagem.main()

        if self.ponto_de_parada==1:
            classe=Historia(self.ponto_de_parada,1,1)
            texto1=classe.historia(self.ponto_de_parada)
            contadorfixo=15
            framesanimação=(len(maga))
            if self.tempo_dialogo>5*self.tempo or self.tempo_dialogo==0:
                if self.frameinit<framesanimação-1:                
                    self.frameinit+=1
                else:
                    self.frameinit=0
                self.win.blit(maga[self.frameinit], (100,325))
            if (len(texto1)*contadorfixo<=self.tempo*contadorfixo) and self.botao_pressionado == True:
                self.ponto_de_parada=0
                self.tempo=0
                self.tempo_dialogo=0
                self.relogio=1
                self.texto_anterior="-"
                self.ponto_de_parada=0
            if len(texto1)*contadorfixo>self.tempo*contadorfixo:
                self.tempo_dialogo+=5
                contador=self.relogio
                if self.tempo_dialogo>contadorfixo*self.relogio:
                    self.relogio+=1
                    self.tempo+=1
                save = self.texto_anterior
                if (self.relogio>contador or self.tempo_dialogo==5) and len(texto1)*contadorfixo>self.tempo*contadorfixo:
                    texto_cortado=texto1[self.tempo]
                    self.texto_anterior+=texto_cortado


            textofinal=font.render(self.texto_anterior, True, (255, 255, 255))
            self.win.blit(tela_falas,(120,580))
            self.win.blit(textofinal,(200,600))

def main():
    jogo = Jogo(1200,800)
    jogo.main()
    pygame.init()


if __name__ == "__main__":
    main()