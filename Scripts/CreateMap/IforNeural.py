import pygame 
import Interface.Constants as ct

#Iterface com Iformaçoes de texto da simulação
class IforNeural():
    def __init__(self) -> None:
        #Construtor
        self.windows = pygame.display.get_surface()
        self.createInterfaceMenu()
        pass
         
    def createInterfaceMenu(self):
        #Criar Interface
        self.backGroundMenuIfor = pygame.image.load(ct.dicImageBut2)
        self.backGroundMenuIfor = pygame.transform.scale(self.backGroundMenuIfor,(350,250))


    def update(self):  
        #Atualizar Frame A Frame     
        self.backgroundMenuButtonsRenderized = self.windows.blit(self.backGroundMenuIfor, (1350,705))
        posButsX,posButsY = self.backgroundMenuButtonsRenderized.topleft

        label = f"Geração:       {ct.generation}"
        bestCar = f"Melhor Carro:      {round(ct.theBest,2)} M"

        if(ct.theBestCar != None):
            isWin = f"Velocidade:       {round(ct.theBestCar.speedInit,2)} Ms"
            self.windows.blit(ct.menuFont.render(isWin,True,"white"),(posButsX + 25,posButsY + 115 )) 
            self.windows.blit(ct.menuFont.render(f"Ganhou:   { ct.isWin }",True,"green"),(posButsX + 25,posButsY + 205 ))

        self.windows.blit(ct.menuFont.render("Neural NetWorking",True,"red"),(posButsX + 100,posButsY + 25 ))        
        self.windows.blit(ct.menuFont.render(label,True,"white"),(posButsX + 25,posButsY + 55 )) 
        self.windows.blit(ct.menuFont.render(bestCar,True,"white"),(posButsX + 25,posButsY + 85 )) 
        self.windows.blit(ct.menuFont.render(f"Tempo da Simulção:  {ct.countTimeLimit}",True,"white"),(posButsX + 25,posButsY + 145 ))
        self.windows.blit(ct.menuFont.render(f"Tempo Total (Segundos):   {round(ct.countTimeLimitAll,2)}",True,"white"),(posButsX + 25,posButsY + 175 ))


