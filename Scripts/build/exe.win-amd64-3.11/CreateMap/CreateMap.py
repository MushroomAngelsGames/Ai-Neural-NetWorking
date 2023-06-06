import pygame 
import Interface.Constants as ct
from pygame.locals import *
import CreateMap.CreateMapMenu as ctMapMenu 

#Controlador do Modo Runtime.
class CreateMap(): 
    def __init__(self) -> None:
        #Construtor
        self.windows = pygame.display.set_mode((ct.gameWidth,ct.gameHeight))
        self.musicGame = pygame.mixer.music.load(".\Music/gameMusic.mp3")
        pygame.mixer.music.play(-1)

        self.createInterfaceMenu()
        self.setSizeStart()    
        pass

    def setSizeStart(self):
        #Definir a Escala de Todos os Objetos do Jogo
        for build in ct.scenaryAll:
            build.item.itemIcone = pygame.transform.scale(build.item.itemIcone, build.item.size)

    def drawAllBuild(self):
        #Desenhar Estradas
        for road in ct.scenaryRoad:           
            self.windows.blit(road.icone,road.pos)
            
        #Desenhar Cenario
        for building in ct.scenaryAll:           
            self.windows.blit(building.icone,building.pos)

    def createInterfaceMenu(self):
        #Criar Interface do Menu
        self.backGroundRoad = pygame.image.load(ct.dicBackGroundImageRoad)
        self.backGroundRoad = pygame.transform.scale(self.backGroundRoad,(ct.gameWidth,ct.gameHeight))
        self.windows.blit(self.backGroundRoad,(0,0))

        #Criar Menu
        self.createMapMenu = ctMapMenu.CreateMapMenu()
        self.createMapMenu.createInterfaceMenu()

    def update(self):
        #Atualizar Jogo
        self.windows.blit(self.backGroundRoad,(0,0))
        self.drawAllBuild()
        self.createMapMenu.update()
   
  
        
        
