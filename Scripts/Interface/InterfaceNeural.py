from typing import Any
import pygame
import Interface.Constants as ct

#Iterface das camadas Neurais
class InterfaceNeural():
    def __init__(self) -> None:
        #Contrutor
        self.windows = pygame.display.get_surface()
        self.createInterfaceMenu()
        self.rede = Rede()   
        pass

    def createInterfaceMenu(self):
        #Criar Iterface Grafica
        self.backGroundMenuIfor = pygame.image.load(ct.dicImageBut2)
        self.backGroundMenuIfor = pygame.transform.scale(self.backGroundMenuIfor,(435,285))
        self.backgroundMenuButtonsRenderized = self.windows.blit(self.backGroundMenuIfor, (25,670))

    def update(self):  
        #Atualzar Interface por Frame     
        self.backgroundMenuButtonsRenderized = self.windows.blit(self.backGroundMenuIfor, (25,670))
       
        if(ct.theFirstCar != None and ct.theFirstCar.neuronController.neuro1 != None ):
            self.rede.setValue(ct.theFirstCar)
            self.rede.update()
            self.defineValues()

    def defineValues(self):
        #Atribuir valores e Exibir na Tela

        posButsX,posButsY = self.backgroundMenuButtonsRenderized.topleft
        labelTop = f"{round(ct.theFirstCar.HelpFromTop.disCount,2)}"
        labelBottom = f"{round(ct.theFirstCar.HelpFromBottom.disCount,2)}"
        labelLeft = f"{round(ct.theFirstCar.HelpFromLeft.disCount,2)}"
        labelRight = f"{round(ct.theFirstCar.HelpFromRight.disCount,2)}"
        labelSpeed= f"{round(ct.theFirstCar.speedInit,2)}"

        labelItemLeft = f"{round(ct.theFirstCar.HelpFromLeftTop.disCount,2)}"
        labelItemRight = f"{round(ct.theFirstCar.HelpFromRightTop.disCount,2)}"
        labelItemTop = f"{round(ct.theFirstCar.HelpFromLeftBottom.disCount,2)}"
        labelItemBottom = f"{round(ct.theFirstCar.HelpFromRightBottom.disCount,2)}"

        labeleaveTop = f"Up:  {True if ct.theFirstCar.neuronController.neuroFoward.valueFinal > 1 else False}"
        labeleaveBottom = f"Down:  {True if ct.theFirstCar.neuronController.neuroBack.valueFinal > 1 else False}"
        labeleaveLeft = f"Left:  {True if ct.theFirstCar.neuronController.neuroTurnLeft.valueFinal > 1 else False}"
        labeleaveRight = f"Right:  {True if ct.theFirstCar.neuronController.neuroTurnRight.valueFinal > 1 else False}"
        labeleaveAccelerate = f"Speed:  {True if ct.theFirstCar.neuronController.neuroSpeed.valueFinal > 1 else False}"
        labelDistance = f"Distancia Alvo:  {ct.theFirstCar.distanceFromGoal} Metros"
        color = "red"
        color2 = "white"
        self.windows.blit(ct.menuFont.render(labelTop,True,color),(posButsX + 25,posButsY + 20)) 
        self.windows.blit(ct.menuFont.render(labelBottom,True,color),(posButsX + 25,posButsY + 48 )) 
        self.windows.blit(ct.menuFont.render(labelLeft,True,color),(posButsX + 25,posButsY + 76 )) 
        self.windows.blit(ct.menuFont.render(labelRight,True,color),(posButsX + 25,posButsY + 104 )) 
        self.windows.blit(ct.menuFont.render(labelSpeed,True,color),(posButsX + 25,posButsY + 132 ))    
        self.windows.blit(ct.menuFont.render(labelItemLeft,True,color),(posButsX + 25,posButsY + 160 )) 
        self.windows.blit(ct.menuFont.render(labelItemRight,True,color),(posButsX + 25,posButsY + 188 )) 
        self.windows.blit(ct.menuFont.render(labelItemTop,True,color),(posButsX + 25,posButsY + 216 )) 
        self.windows.blit(ct.menuFont.render(labelItemBottom,True,color),(posButsX + 25,posButsY + 244 ))

        self.windows.blit(ct.menuFont.render(labeleaveTop,True,color2),(posButsX + 325,posButsY + 70 )) 
        self.windows.blit(ct.menuFont.render(labeleaveBottom,True,color2),(posButsX + 325,posButsY + 100 )) 
        self.windows.blit(ct.menuFont.render(labeleaveLeft,True,color2),(posButsX + 325,posButsY + 130 )) 
        self.windows.blit(ct.menuFont.render(labeleaveRight,True,color2),(posButsX + 325,posButsY + 160 ))
        self.windows.blit(ct.menuFont.render(labeleaveAccelerate,True,color2),(posButsX + 325,posButsY + 190 ))
        self.windows.blit(ct.menuFont.render(labelDistance,True,color2),(posButsX + 150,posButsY + 250 ))

#Interface de Sprite das Ligações Neurais
class Rede():
    def __init__(self) -> None:
        #Construtor
        self.sprites = []
        self.windows = pygame.display.get_surface()
        self.sprites.append(pygame.image.load(".\Imagens\Rede/BASE.png"))
        self.sprites.append(pygame.image.load(".\Imagens\Rede/N1.png"))
        self.sprites.append(pygame.image.load(".\Imagens\Rede/N2.png"))
        self.sprites.append(pygame.image.load(".\Imagens\Rede/N3.png"))
        self.sprites.append(pygame.image.load(".\Imagens\Rede/N4.png"))
        self.sprites.append(pygame.image.load(".\Imagens\Rede/N5.png"))
        self.sprites.append(pygame.image.load(".\Imagens\Rede/N6.png"))

        size = (707/3,732/3)
        self.sprites[0] = pygame.transform.scale(self.sprites[0] ,size)
        self.sprites[1] = pygame.transform.scale(self.sprites[1] ,size)
        self.sprites[2] = pygame.transform.scale(self.sprites[2] ,size)
        self.sprites[3] = pygame.transform.scale(self.sprites[3] ,size)
        self.sprites[4] = pygame.transform.scale(self.sprites[4] ,size)
        self.sprites[5] = pygame.transform.scale(self.sprites[5] ,size)
        self.sprites[6] = pygame.transform.scale(self.sprites[6] ,size)

        self.neuro1 = None
        self.neuro2 = None
        self.neuro3 = None
        self.neuro4 = None
        self.neuro5 = None
        self.neuro6 = None
    
    def setValue(self,car):
        #Atibuir Valore de Saídas dos Neuronios
        self.neuro1 = car.neuronController.neuro1.valueHelpInterface
        self.neuro2 = car.neuronController.neuro2.valueHelpInterface  
        self.neuro3 = car.neuronController.neuro3.valueHelpInterface  
        self.neuro4 = car.neuronController.neuro4.valueHelpInterface 
        self.neuro5 = car.neuronController.neuro5.valueHelpInterface  
        self.neuro6 = car.neuronController.neuro6.valueHelpInterface  

    def update(self) -> None:
        #Atualizar Por Frame
        self.windows.blit(self.sprites[0],(100,695)) 

        if(self.neuro1 == 1):
            self.windows.blit(self.sprites[1],(100,695)) 
        if(self.neuro2 == 1):
            self.windows.blit(  self.sprites[2] ,(100,695)) 
        if(self.neuro3 == 1):
            self.windows.blit(self.sprites[3] ,(100,695)) 
        if(self.neuro4 == 1):
            self.windows.blit(self.sprites[4] ,(100,695)) 
        if(self.neuro5 == 1):
            self.windows.blit( self.sprites[5],(100,695)) 
        if(self.neuro6 == 1):
            self.windows.blit(self.sprites[6],(100,695)) 
        
    
        