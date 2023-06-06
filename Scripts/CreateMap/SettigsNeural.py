import pygame 
import Interface.Button as bt
from pygame.locals import *
import Interface.Constants as ct

#Configurar Rede Neural em Simulação
class SettigsNeural():
    def __init__(self,parent) -> None:
        #Construtor
        self.windows = pygame.display.get_surface()
        self.createInterfaceMenu()
        self.parent = parent
        self.typeModeCar = "Morrer"

        if(ct.typeBias == 1):
            self.typeBiasLabel = "Fixo"
        elif(ct.typeBias == 2):
            self.typeBiasLabel = "Disable"
        else:
            self.typeBiasLabel = "Random"
        pass

    def createInterfaceMenu(self):
        #Criar Interface

        self.buttonModelImage = pygame.image.load(ct.dicImageBut1)
        self.buttonModelImage = pygame.transform.scale(self.buttonModelImage,(25,25))
        
        
        self.backGroundMenuIfor = pygame.image.load(ct.dicImageBut2)
        self.backGroundMenuIfor = pygame.transform.scale(self.backGroundMenuIfor,(320,235))
        self.buttonModelImage1 = pygame.transform.scale(self.backGroundMenuIfor,(100,35))

        self.backgroundMenuButtonsRenderized = self.windows.blit(self.backGroundMenuIfor, (25,25))
        posButsX,posButsY = self.backgroundMenuButtonsRenderized.topleft

        self.butMorePopulation = bt.Button(self.buttonModelImage,posButsX  + 260 ,posButsY + 65,"+",self.windows)
        self.butLessPopulation = bt.Button(self.buttonModelImage,posButsX + 290,posButsY + 65,"-",self.windows)

        self.butMoreTime= bt.Button(self.buttonModelImage,posButsX  + 260 ,posButsY + 100,"+",self.windows)
        self.butLessTime = bt.Button(self.buttonModelImage,posButsX + 290,posButsY + 100,"-",self.windows)

        self.butMoreMutationFactor= bt.Button(self.buttonModelImage,posButsX  + 260 ,posButsY + 30,"+",self.windows)
        self.butLessMutationFactor = bt.Button(self.buttonModelImage,posButsX + 290,posButsY + 30,"-",self.windows)

        self.butMoreType= bt.Button(self.buttonModelImage,posButsX  + 260 ,posButsY + 135,"+",self.windows)
        self.butLessType = bt.Button(self.buttonModelImage,posButsX + 290,posButsY + 135,"-",self.windows)
        
        self.butModeCar =  bt.Button(self.buttonModelImage1,posButsX  + 255 ,posButsY + 210,"TROCAR",self.windows)
        self.butTypeBias =  bt.Button(self.buttonModelImage1,posButsX  + 255 ,posButsY + 170,"TROCAR",self.windows)
       

    def controllerButs(self):
        #Atualzar Botoes
        mousePos = pygame.mouse.get_pos()
        self.butModeCar.update()
        self.butModeCar.onMouseEnter(mousePos)
        self.butTypeBias.update()
        self.butTypeBias.onMouseEnter(mousePos)
        self.butMoreType.update()
        self.butMoreType.onMouseEnter(mousePos)
        self.butLessType.update()
        self.butLessType.onMouseEnter(mousePos)
        self.butMorePopulation.update()
        self.butMorePopulation.onMouseEnter(mousePos)
        self.butMoreTime.update()
        self.butMoreTime.onMouseEnter(mousePos)
        self.butLessTime.update()
        self.butLessTime.onMouseEnter(mousePos)
        self.butLessPopulation.update()
        self.butLessPopulation.onMouseEnter(mousePos)
        self.butMoreMutationFactor.update()
        self.butMoreMutationFactor.onMouseEnter(mousePos)
        self.butLessMutationFactor.update()
        self.butLessMutationFactor.onMouseEnter(mousePos)

    def eventsButs(self):
        #Verificar Interação com Botoes
        mousePos = pygame.mouse.get_pos()

        if self.butModeCar.checkInput(mousePos):
            #self.parent.resetTheBetter();
            if(ct.modeCar == 0):
                ct.modeCar = 1
                self.typeModeCar = "Morrer"
            elif(ct.modeCar == 1):
                ct.modeCar = 0
                self.typeModeCar = "Reagir"
        

        if self.butTypeBias.checkInput(mousePos):
            
            if(ct.typeBias == 0):
                ct.typeBias = 1
                self.typeBiasLabel = "Fixo"
            elif(ct.typeBias == 1):
                ct.typeBias = 2
                self.typeBiasLabel = "Disable"
            else:
                ct.typeBias = 0
                self.typeBiasLabel = "Random"
            


        if self.butMoreType.checkInput(mousePos) and ct.typeCamadas < 3:
            self.parent.resetTheBetter()
            ct.typeCamadas += 1

        if self.butLessType.checkInput(mousePos) and ct.typeCamadas > 1:
            self.parent.resetTheBetter()
            ct.typeCamadas -= 1

        if self.butLessMutationFactor.checkInput(mousePos):
            ct.mutationFactor -=0.001
            ct.mutationFactor = abs(ct.mutationFactor)

        if self.butMoreMutationFactor.checkInput(mousePos):
             ct.mutationFactor +=0.001
             ct.mutationFactor = abs(ct.mutationFactor)

        if self.butMorePopulation.checkInput(mousePos):
            ct.population+=50

        if self.butLessPopulation.checkInput(mousePos) and ct.population > 25:
            ct.population-=50

        if self.butLessTime.checkInput(mousePos) and ct.timeLimit > 50:
            ct.timeLimit-=50

        if self.butMoreTime.checkInput(mousePos):
            ct.timeLimit+=50

    def update(self): 
        #Atualizar Frame a Frame      
        self.backgroundMenuButtonsRenderized = self.windows.blit(self.backGroundMenuIfor, (25,25))
        posButsX,posButsY = self.backgroundMenuButtonsRenderized.topleft

        self.controllerButs()

        self.windows.blit(ct.menuFont.render(f"Fator X:     {round(ct.mutationFactor,5)}",True,"white"),(posButsX + 25,posButsY + 25 ))
        self.windows.blit(ct.menuFont.render(f"População:     {ct.population}",True,"white"),(posButsX + 25,posButsY + 55 )) 
        self.windows.blit(ct.menuFont.render(f"Tempo Máximo:     {ct.timeLimit}",True,"white"),(posButsX + 25,posButsY + 85 ))  
        self.windows.blit(ct.menuFont.render(f"Camadas Ocultas:     {ct.typeCamadas}",True,"white"),(posButsX + 25,posButsY + 115 ))  
        self.windows.blit(ct.menuFont.render(f"Tipo de Vies: {self.typeBiasLabel}",True,"white"),(posButsX + 25,posButsY + 160 ))  
        self.windows.blit(ct.menuFont.render(f"Mov. Final: {self.typeModeCar}",True,"white"),(posButsX + 25,posButsY + 195 ))  
