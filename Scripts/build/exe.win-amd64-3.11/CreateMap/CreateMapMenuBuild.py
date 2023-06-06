import pygame 
import CreateMap.Build as bd
import CreateMap.IforItem as ifitem
import Interface.Constants as ct
import Interface.Button as bt
from pygame.locals import *

#Controlador da Construção
class CreateMapMenuBuild():
    def __init__(self,father) -> None:
        #Construtor
        self.windows = pygame.display.get_surface()
        self.createInterfaceMenu()
        self.stateBuild = False
        self.father = father
        pass

    def createInterfaceMenu(self):
        #Criar Menus
        self.buttonModelImage = pygame.image.load(ct.dicImageBut2)
        self.buttonModelImage = pygame.transform.scale(self.buttonModelImage,(85,85))

        self.backGroundMenu = pygame.image.load(ct.dicBackGroundImageMenu)
        self.backGroundMenu = pygame.transform.scale(self.backGroundMenu,(ct.gameWidth + 10,100))
        self.backgroundMenuButtonsRenderized = self.windows.blit(self.backGroundMenu,(-5,885))
        
        posButsX,posButsY = self.backgroundMenuButtonsRenderized.topleft

        #Shope de Itens
        for item in ct.itemBuild:
            item.itemIcone = pygame.transform.scale(item.itemIcone,(50,50))
            item.But = bt.Button(self.buttonModelImage,posButsX + 50 + (item.id * 90), posButsY + 50,item.name,self.windows,iconBut=item.itemIcone,panding=25)

    def controllerButs(self):
        #Verificar Item Selecionado
        for item in ct.itemBuild:
            item.But.update()
            if item.But.onMouseEnter(pygame.mouse.get_pos()):
                ifitem.iforItem(item)
            if(pygame.mouse.get_pressed()[0]):
                if item.But.checkInput(pygame.mouse.get_pos()) == True:
                    self.father.inBuild = True
                    self.father.itemBuildController = bd.Build(item)
                    self.father.itemBuildController.timeBuild = 0
                    
    def update(self):
        #Atualizar
        self.backgroundMenuButtonsRenderized = self.windows.blit(self.backGroundMenu,(-5,885))
        self.controllerButs()