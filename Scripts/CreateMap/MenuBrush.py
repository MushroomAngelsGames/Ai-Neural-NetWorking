import pygame 
import Interface.Constants as ct

#Controlador do Tamanho do Pincel
class MenuBrush():
    def __init__(self) -> None:
        #construtor
        self.windows = pygame.display.get_surface()
        pass

    def createInterfaceMenu(self):
        #Criar Interface dos Menus
        self.backGroundMenuIfor = pygame.image.load(ct.dicBackGroundImageMenu4)
        self.backGroundMenuIfor = pygame.transform.scale(self.backGroundMenuIfor,(500,45))
        self.backGroundMenuIforRenderized = self.windows.blit(self.backGroundMenuIfor,(1220,890))
        self.labelText = ct.menuFont.render(ct.labelBrush,True,"white")
        posButsX,posButsY = self.backGroundMenuIforRenderized.topleft
        self.windows.blit(self.labelText,(posButsX + 10 ,posButsY + 10))
        
    
    def update(self):
        #Atualizar Frame a Frame
        self.createInterfaceMenu()
       