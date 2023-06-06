import pygame 
import CreateMap.IforNeural as iforNeu
import CreateMap.SettigsNeural as setttigs
import Interface.Constants as ct
import Interface.Button as bt
import Interface.InterfaceNeural as neural
from pygame.locals import *

#Controlador Menu Game
class MenuInGame():
    def __init__(self,parent) -> None:
        self.windows = pygame.display.get_surface()
        self.createInterfaceMenu()
        self.menuIforNeural = iforNeu.IforNeural()
        self.menuSettigs = setttigs.SettigsNeural(parent)
        self.camadas = neural.InterfaceNeural()
        self.isOpenIforNeu = True
        self.isSettigs = True
        self.isCamadas = True
        pass

    def eventsButs(self):
        #Verificar Botões
        mousePos = pygame.mouse.get_pos()
        if self.buttonButOpenSettigs.checkInput(mousePos):
            self.isSettigs = True if self.isSettigs == False else False

        if self.buttonButPauser.checkInput(mousePos):
            ct.inPause = True if ct.inPause == False else False

        if self.buttonButOpenNeuralNetworking.checkInput(mousePos):
            self.isOpenIforNeu = True if self.isOpenIforNeu == False else False
        
        if self.buttonButOpenNeural.checkInput(mousePos):
            self.isCamadas = True if self.isCamadas == False else False

        if self.butRestart.checkInput(mousePos):
            ct.countTimeLimit +=500000000000

    def controllerButs(self):
        #Atualizar Botões
        mousePos = pygame.mouse.get_pos()
        self.backgroundMenuButtonsRenderized = self.windows.blit(self.backgroundMenuButtons,(1510,25))
        self.buttonButOpenNeuralNetworking.update()
        self.buttonButOpenNeuralNetworking.onMouseEnter(mousePos)
        self.buttonButOpenSettigs.update()
        self.buttonButOpenSettigs.onMouseEnter(mousePos)
        self.buttonButOpenNeural.update()
        self.buttonButOpenNeural.onMouseEnter(mousePos)
        self.buttonButPauser.update()
        self.buttonButPauser.onMouseEnter(mousePos)
        self.butRestart.update()
        self.butRestart.onMouseEnter(mousePos)

    def createInterfaceMenu(self):
        #Criar Menu da Simulação
        self.buttonModelImage = pygame.image.load(ct.dicImageBut2)
        self.buttonModelImage = pygame.transform.scale(self.buttonModelImage,(170,35))

        self.backgroundMenuButtons = pygame.image.load(ct.dicImageBut2)
        self.backgroundMenuButtons = pygame.transform.scale(self.backgroundMenuButtons,(190,215))
        self.backgroundMenuButtonsRenderized = self.windows.blit(self.backgroundMenuButtons,(1510,20))
        
        posButsX,posButsY = self.backgroundMenuButtonsRenderized.topright

        self.buttonButOpenNeuralNetworking= bt.Button(self.buttonModelImage,posButsX - 95,posButsY + 30,"REDE NEURAL",self.windows)
        self.buttonButOpenSettigs = bt.Button(self.buttonModelImage,posButsX - 95,posButsY + 70,"VALORES",self.windows)
        self.buttonButOpenNeural= bt.Button(self.buttonModelImage,posButsX - 95,posButsY + 110,"CAMADAS",self.windows)
        self.buttonButPauser= bt.Button(self.buttonModelImage,posButsX - 95,posButsY + 150, "PAUSER",self.windows)
        self.butRestart= bt.Button(self.buttonModelImage,posButsX - 95 ,posButsY + 190,"RESTART",self.windows)

    def update(self):
        #Atualizar todos os Frames
        self.controllerButs()

        if(self.isOpenIforNeu):
            self.menuIforNeural.update()

        if(self.isSettigs):
            self.menuSettigs.update()

        if(self.isCamadas):
            self.camadas.update()

        self.buttonButPauser.labelInput  = "PAUSER" if  ct.inPause == False else "RESUME"

        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.eventsButs()
                if(self.isSettigs):
                    self.menuSettigs.eventsButs()