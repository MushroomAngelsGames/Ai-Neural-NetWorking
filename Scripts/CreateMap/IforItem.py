import pygame 
import Interface.Constants as ct
from pygame.locals import *

#Controlador do Menu que Informa o Tipo de Item de Construção
class iforItem():
    def __init__(self,itemValue) -> None:
        #Construtor
        self.windows = pygame.display.get_surface()
        self.itemBuild = itemValue
        self.createInterfaceMenu()
        pass

    def createInterfaceMenu(self):
        #Criar Menu com As Iformações do Item
        self.backGroundMenuIfor = pygame.image.load(ct.dicBackGroundImageMenu4)
        self.backGroundMenuIfor = pygame.transform.scale(self.backGroundMenuIfor,(600,75))
        self.backgroundMenuButtonsRenderized = self.windows.blit(self.backGroundMenuIfor,(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1] - 150))
        
        posButsX,posButsY = self.backgroundMenuButtonsRenderized.topleft

        self.labelText = ct.menuFont.render(self.itemBuild.descriptionItem,True,"white")
        self.labelTextTitle = ct.menuFont.render(self.itemBuild.name,True,"white")
        
        self.windows.blit(self.labelText,(posButsX + 45 ,posButsY + 35))
        self.windows.blit(self.labelTextTitle,(posButsX + 35 ,posButsY + 10))


