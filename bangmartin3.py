import pygame 
pygame.init()
ALTURA=1200
LARGURA=800
win=pygame.display.set_mode((ALTURA,LARGURA))
pygame.display.set_caption("alo")
x=50
y=50
width=60
height=40
vel=5
p1=0
p2=0
lista_num=5
diference = [0,0]
once = True
carregando = False
background = pygame.image.load("background.png")
salty=pygame.image.load("salty.png")
candy=pygame.image.load("candy.png")
hot=pygame.image.load("hot.png")
tasty=pygame.image.load("tasty.png")
sour=pygame.image.load("sour.png")
quadrado_quant=pygame.image.load("quadrado2.png")
tamanhos=[[60,80],[50,70],[40,55],[25,70],[40,50]]
tamanhos_quad=[[10,160],[10,265],[10,370],[10,475],[10,580]]
mistura=[]
reset=pygame.image.load("reset.png")
mandar=pygame.image.load("mandar.png")
pygame.init() 
qt1=0
qt2=0
qt3=0
qt4=0
qt5=0
white = (255, 255, 255) 
lista_lugares=[[480,280],[540,292],[590,300],[635,290],[665,310]]
font = pygame.font.SysFont(None, 40)
display_surface = pygame.display.set_mode((ALTURA, LARGURA )) 
b = pygame.mixer.Sound("sound0.ogg")
a = pygame.mixer.Sound("sound.ogg")
tela_sea=pygame.image.load("seawater.png")
tela_heavy=pygame.image.load("heavydrink.png")
tela_sugar=pygame.image.load("sugarrush.png")
tela_nao_deu=pygame.image.load("naodeucerto.png")
tela_certo=0
tela_errado=False

# infinite loop 
while True : 
    mouse = pygame.mouse.get_pressed()
    mousepos=pygame.mouse.get_pos()
    for event in pygame.event.get() : 

        if event.type == pygame.QUIT : 
              pygame.quit() 
              quit() 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if mousepos[0]>10 and mousepos[0]<10+100:
                if mousepos[1]>30 and mousepos[1]<30+50:
                    if qt1>((qt1+qt2+qt3+qt4+qt5)*0.6): 
                        print("Sea Water")
                        qt1=0
                        qt2=0
                        qt3=0
                        qt4=0
                        qt5=0
                        tela_certo=1

                    elif qt3>((qt1+qt2+qt3+qt4+qt5)*0.2) and qt4>((qt1+qt2+qt3+qt4+qt5)*0.2): 
                        print("Heavy Drink")
                        qt1=0
                        qt2=0
                        qt3=0
                        qt4=0
                        qt5=0
                        tela_certo=2

                    elif qt2>((qt1+qt2+qt3+qt4+qt5)*0.8): 
                        print("Sugar Rush")
                        qt1=0
                        qt2=0
                        qt3=0
                        qt4=0
                        qt5=0
                        tela_certo=3

                    else:
                        print("Nada deu certo")
                        qt1=0
                        qt2=0
                        qt3=0
                        qt4=0
                        qt5=0
                        tela_certo=4
            if mousepos[0]>10 and mousepos[0]<10+100:
                if mousepos[1]>90 and mousepos[1]<90+50:
                    qt1=0
                    qt2=0
                    qt3=0
                    qt4=0
                    qt5=0


  
        pygame.display.update()  


    if mouse == (1,0,0):
        for x in range(5):
            if mousepos[0]>lista_lugares[x][0] and mousepos[0]<lista_lugares[x][0]+tamanhos[x][0]:
                if mousepos[1]>lista_lugares[x][1] and mousepos[1]<lista_lugares[x][1]+tamanhos[x][1]:
                    if once == True:
                        diference = [mousepos[0]-lista_lugares[x][0],mousepos[1]-lista_lugares[x][1]]
                        once = False
                        lista_num=x
                    carregando = True
    else:
        if once == False:
            lista_lugares = [[480,280],[540,292],[590,300],[635,290],[665,310]]
            if (mousepos[0]>458 and mousepos[0]<564) and (mousepos[1]>410 and mousepos[1]<546):
                if lista_num == 0 and mistura.count(0)<9:
                    pygame.mixer.Sound.play(a)
                    qt1+=1
                elif lista_num == 1 and mistura.count(1)<9:
                    pygame.mixer.Sound.play(b)
                    qt2+=1
                elif lista_num == 2 and mistura.count(2)<9:
                    pygame.mixer.Sound.play(b)
                    qt3+=1
                elif lista_num == 3 and mistura.count(3)<9:
                    pygame.mixer.Sound.play(b)
                    qt4+=1
                elif lista_num == 4 and mistura.count(4)<9:
                    pygame.mixer.Sound.play(b)
                    qt5+=1

        once = True
        carregando = False
    


    if carregando == True:
            lista_lugares[lista_num][0]=mousepos[0]-diference[0]
            lista_lugares[lista_num][1]=mousepos[1]-diference[1]

    
    win.fill((20,20,180))
    win.blit(background,(0,0))
    win.blit(quadrado_quant,(tamanhos_quad[0]))
    win.blit(quadrado_quant,(tamanhos_quad[1]))
    win.blit(quadrado_quant,(tamanhos_quad[2]))
    win.blit(quadrado_quant,(tamanhos_quad[3]))
    win.blit(quadrado_quant,(tamanhos_quad[4]))
    win.blit(mandar,(10,30))
    win.blit(reset,(10,90))
    win.blit(salty,(lista_lugares[0]))
    win.blit(candy,(lista_lugares[1]))
    win.blit(sour,(lista_lugares[2]))
    win.blit(hot,(lista_lugares[3]))
    win.blit(tasty,(lista_lugares[4]))

    text=font.render(str(qt1), True, (255, 255, 255))
    win.blit(text,(tamanhos_quad[0][0]+75,tamanhos_quad[0][1]+70))

    text2=font.render(str(qt2), True, (255, 255, 255))
    win.blit(text2,(tamanhos_quad[1][0]+75,tamanhos_quad[1][1]+70))

    text3=font.render(str(qt3), True, (255, 255, 255))
    win.blit(text3,(tamanhos_quad[2][0]+75,tamanhos_quad[2][1]+70))

    text4=font.render(str(qt4), True, (255, 255, 255))
    win.blit(text4,(tamanhos_quad[3][0]+75,tamanhos_quad[3][1]+70))

    text5=font.render(str(qt5), True, (255, 255, 255))
    win.blit(text5,(tamanhos_quad[4][0]+75,tamanhos_quad[4][1]+70))

    if tela_certo!=0:
        if tela_certo==1:
            win.blit(tela_sea,(LARGURA//2-100,ALTURA//2-300))
        if tela_certo==2:
            win.blit(tela_heavy,(LARGURA//2-100,ALTURA//2-300))
        if tela_certo==3:
            win.blit(tela_sugar,(LARGURA//2-100,ALTURA//2-300))
        if tela_certo==4:
            win.blit(tela_nao_deu,(LARGURA//2-100,ALTURA//2-300))
        for event in pygame.event.get() : 
            if event.type == pygame.MOUSEBUTTONDOWN:
                tela_certo=0


    win.blit(salty,(tamanhos_quad[0][0]+20,tamanhos_quad[0][1]+10))
    win.blit(candy,(tamanhos_quad[1][0]+20,tamanhos_quad[1][1]+10))
    win.blit(sour,(tamanhos_quad[2][0]+25,tamanhos_quad[2][1]+20))
    win.blit(hot,(tamanhos_quad[3][0]+40,tamanhos_quad[3][1]+10))
    win.blit(tasty,(tamanhos_quad[4][0]+25,tamanhos_quad[4][1]+20))


    pygame.display.update()