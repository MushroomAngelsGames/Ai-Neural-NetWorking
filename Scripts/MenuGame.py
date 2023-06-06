import pygame 
import CreateMap.CreateMap as cmap
import Interface.Constants as ct
import Interface.Button as bt
from pygame.locals import *
import webbrowser
from sys import exit

#Controlador da Interface
class StartMenuGame:
    def __init__(self) -> None:  
        #Construtor     
        pygame.init()
        ct.menuFont = pygame.font.SysFont("gabriola",25,True,False)
        self.backGround = []
        self.RestartMenu()
        self.count = 0
        self.valueBackGround = False
        self.clockFps = pygame.time.Clock()
        self.status = 0

        pygame.mixer.music.set_volume(0.1)
        self.musicMenu = pygame.mixer.music.load(".\Music/menu.mp3")
        pygame.mixer.music.play(-1)


        self.currectBackGroundId =0
        pass

    def RestartMenu(self):
        #Inicializar Menu / Restaurar Menu 
        self.setCondigureGame()
        self.createInterfaceMenu()

    def setCondigureGame(self):
        #Definir Nome e Tamanho da Tela.
        self.windows = pygame.display.set_mode((ct.menuWidth,ct.menuHeight))
        pygame.display.set_caption(ct.nameGameForNameWindow)

    def createInterfaceMenu(self):
        #Criar Interface Gráfica
        self.backGround.append(pygame.image.load(ct.dicBackGroundImageMenu1))
        self.backGround.append(pygame.image.load(ct.dicBackGroundImageMenu2))
        self.backGround.append(pygame.image.load(ct.dicBackGroundImageMenu5))
        self.backGround[0] =  pygame.transform.scale(self.backGround[0],(ct.menuWidth,ct.menuHeight)) 
        self.backGround[1] =  pygame.transform.scale(self.backGround[1],(ct.menuWidth,ct.menuHeight)) 
        self.backGround[2] =  pygame.transform.scale(self.backGround[2],(ct.menuWidth,ct.menuHeight)) 

        self.buttonModelImage = pygame.image.load(ct.dicImageBut1)
        self.buttonModelImage = pygame.transform.scale(self.buttonModelImage,(200,50))
        self.buttonExitGame = bt.Button(self.buttonModelImage,150,ct.menuHeight/2 + 235,"SAIR",self.windows)
        self.buttonOtherGames = bt.Button(self.buttonModelImage,150,ct.menuHeight/2 + 180,"OUTROS JOGOS",self.windows)
        self.buttonStartGame = bt.Button(self.buttonModelImage,150,ct.menuHeight/2 + 125,"JOGAR",self.windows)

    def animateBackGround(self):
        #Animmar Fundo do Menu.
        self.count+=1
        if(self.count == 15):
            self.count = 0
            if(self.currectBackGroundId == 2):
                self.currectBackGroundId = 0
            else:
                self.currectBackGroundId+=1

        self.windows.blit((self.backGround[ self.currectBackGroundId]),(0,0))
      
    def controllerButs(self):
        #Atualizar Botões Dessa Iterface Por Frame
        posMouse = pygame.mouse.get_pos()
        self.buttonOtherGames.update()
        self.buttonOtherGames.onMouseEnter(posMouse)
        self.buttonStartGame.update()
        self.buttonStartGame.onMouseEnter(posMouse)
        self.buttonExitGame.update()
        self.buttonExitGame.onMouseEnter(posMouse)
    
    def eventsButs(self):
        #Verificar Interação do Player com os Botões
        posMouse = pygame.mouse.get_pos()
        if self.buttonStartGame.checkInput(posMouse):
            self.GlobalGameCreateMap = cmap.CreateMap()
            self.status = 1

        if self.buttonOtherGames.checkInput(posMouse):
            webbrowser.open("https://store.steampowered.com/publisher/luiz-felipe-da-silva-marian/",new=1)

        if self.buttonExitGame.checkInput(posMouse):
            exit()

    def modeGame(self):
        #Verificar Se Esta no Menu ou no Jogo.
        if self.status == 0:
            self.windows.fill((0,0,0))
            self.animateBackGround()
            self.controllerButs()
        elif self.status == 1:
            self.GlobalGameCreateMap.update()

    def update(self):
        #Atualizar Tudo.
        while True:     
            self.clockFps.tick(ct.fps)
            self.modeGame()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.status == 0:
                        self.eventsButs()
                
      
            pygame.display.flip()

#Inicializar a Classe MAIN do Software.
GlobalGame = StartMenuGame()
GlobalGame.update()