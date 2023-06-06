import pygame
import Neural.Neuron as neuron
import random as rd
import math as mt
import Interface.Constants as ct

#Controle dos carros
class Car():
    def __init__(self,speed,posStart,isFirst,parent) -> None:   
        #Inicializar Carro
        self.windows = pygame.display.get_surface()
        self.carColor =(rd.randint(0,255),rd.randint(0,125),rd.randint(0,255))  
        self.lastColor  = self.carColor
 
        self.speedInit = speed
        self.pos = posStart
    
        self.isFirst = isFirst

        self.HelpFromTop = HelpCheckDistanceAndObjectCollider()
        self.HelpFromBottom = HelpCheckDistanceAndObjectCollider()
        self.HelpFromLeft = HelpCheckDistanceAndObjectCollider()
        self.HelpFromRight = HelpCheckDistanceAndObjectCollider()

        self.HelpFromLeftTop = HelpCheckDistanceAndObjectCollider()
        self.HelpFromRightTop = HelpCheckDistanceAndObjectCollider()
        self.HelpFromLeftBottom = HelpCheckDistanceAndObjectCollider()
        self.HelpFromRightBottom = HelpCheckDistanceAndObjectCollider()

        self.countLimitStop = 0
        self.timeNewCheck = 5
        self.valueActivetion = 1
        self.countCheckPoint = 0
        self.crashCar = False
        self.isWin= False 

        self.listPosWalked = []
        self.distanceFromGoal = 150000
        self.parent =parent
        self.carRenderized = pygame.draw.circle(self.windows,(0,255,0),(self.pos[0],self.pos[1]),ct.scaleCar)
        self.neuronController = neuron.NeuronController(self,parent.BetterWeights)
            
        pass

    def checkCollisionPos(self,pos):
        #Verificar se Carro deve Morrer fora do Mapa
        if(pos[0] < 0 or pos[1] < 0 or pos[0] >= ct.gameWidth or pos[1] >= ct.gameHeight):
            self.crashCar = True
            return True, 1
        
        id = ct.mapId[pos] 
        if(id != 0):
            return True,id

        return False,id
    
    def checkCrash(self):
        #Verificar se Carro deve Morrer

        if(self.pos[0] < 0 or self.pos[1] < 0 or self.pos[0] >= ct.gameWidth or self.pos[1] >= ct.gameHeight):
            self.crashCar = True
    
        id = ct.mapId[self.pos]

        if(id==1):
            self.crashCar = True
        elif(id==3):
            self.isWin = True
            self.parent.setEffectWin()
            ct.countFinish +=1
            self.crashCar = True
            self.checkDistanceFromGoal()
            return True
        
        if(self.crashCar and self.isWin == False):
            self.parent.listCarsDead.append(self)
            self.parent.listCars.remove(self)
            self.checkDistanceFromGoal()
            return True
      
        return False

    def checkSpeed(self):
        #Verificar Colisao com Item de Velocidade
        id = ct.mapId[self.pos]
        if(id == 4):
           self.speedInit += 2 if self.speedInit < 25 else 25

        if(id == 5):
           self.speedInit -= 2 if self.speedInit >  10 else 1 

    def checkPosition(self):
        #Sensores do Carro
        self.HelpFromTop.resetCheck()
        self.HelpFromBottom.resetCheck()
        self.HelpFromLeft.resetCheck()
        self.HelpFromRight.resetCheck()

        self.HelpFromLeftTop.resetCheck()
        self.HelpFromRightTop.resetCheck()
        self.HelpFromLeftBottom.resetCheck()
        self.HelpFromRightBottom.resetCheck()


        #Vertice
        self.HelpFromLeftTop.disCount =0
        while self.HelpFromLeftTop.distaceFromCollider == -1:
            hasCollision, item = self.checkCollisionPos((self.carRenderized.centerx -  self.HelpFromLeftTop.disCount,(self.carRenderized.centery) - self.HelpFromLeftTop.disCount))
            if hasCollision:
                self.HelpFromLeftTop.updateValue(item)
            self.HelpFromLeftTop.disCount+=1

        self.HelpFromRightTop.disCount =0
        while self.HelpFromRightTop.distaceFromCollider == -1:
            hasCollision, item = self.checkCollisionPos((self.carRenderized.centerx + self.HelpFromRightTop.disCount,(self.carRenderized.centery) - self.HelpFromRightTop.disCount))
            if hasCollision:
                self.HelpFromRightTop.updateValue(item)
            self.HelpFromRightTop.disCount+=1

        self.HelpFromLeftBottom.disCount =0
        while self.HelpFromLeftBottom.distaceFromCollider == -1:
            hasCollision, item = self.checkCollisionPos((self.carRenderized.centerx - self.HelpFromLeftBottom.disCount,(self.carRenderized.centery) + self.HelpFromLeftBottom.disCount))
            if hasCollision:
                self.HelpFromLeftBottom.updateValue(item)
            self.HelpFromLeftBottom.disCount+=1

        self.HelpFromRightBottom.disCount =0
        while self.HelpFromRightBottom.distaceFromCollider == -1:
            hasCollision, item = self.checkCollisionPos((self.carRenderized.centerx + self.HelpFromRightBottom.disCount,(self.carRenderized.centery) + self.HelpFromRightBottom.disCount))
            if hasCollision:
                self.HelpFromRightBottom.updateValue(item)
            self.HelpFromRightBottom.disCount+=1

        #Normal
        self.HelpFromTop.disCount =0
        while self.HelpFromTop.distaceFromCollider == -1:
            hasCollision, item = self.checkCollisionPos((self.carRenderized.centerx,(self.carRenderized.centery) - self.HelpFromTop.disCount))
            if hasCollision:
                self.HelpFromTop.updateValue(item)
            self.HelpFromTop.disCount+=1

        self.HelpFromBottom.disCount =0
        while self.HelpFromBottom.distaceFromCollider == -1:
            hasCollision, item = self.checkCollisionPos((self.carRenderized.centerx,(self.carRenderized.centery)  +  self.HelpFromBottom.disCount))
            if hasCollision:
                self.HelpFromBottom.updateValue(item)
            self.HelpFromBottom.disCount+=1

        self.HelpFromLeft.disCount =0
        while self.HelpFromLeft.distaceFromCollider == -1:      
            hasCollision, item = self.checkCollisionPos(((self.carRenderized.centerx) - self.HelpFromLeft.disCount,self.carRenderized.centery))
            if hasCollision:
                self.HelpFromLeft.updateValue(item)
            self.HelpFromLeft.disCount+=1

        self.HelpFromRight.disCount =0
        while self.HelpFromRight.distaceFromCollider == -1:         
            hasCollision, item = self.checkCollisionPos(((self.carRenderized.centerx) + self.HelpFromRight.disCount,self.carRenderized.centery))
            if hasCollision:
                self.HelpFromRight.updateValue(item)
            self.HelpFromRight.disCount+=1

    def checkDistanceFromGoal(self):
        #Verificar Distancia do Carro até o Objetivo
        for x in range(ct.scaleCar) :
            for y in range(ct.scaleCar) :
                if((self.pos[0] + x,self.pos[1] + y) in ct.mapIdDistaceFromEnd):
                    self.distanceFromGoal = ct.mapIdDistaceFromEnd[(self.pos[0] + x,self.pos[1] + y)]
                    break

        
        if self.crashCar == False:
            if((self.distanceFromGoal < ct.theFirstCar.distanceFromGoal and  ct.theFirstCar != self) or ct.theFirstCar.crashCar):
                ct.theFirstCar = self
                self.carColor = ct.carColorBetter
            elif (ct.theFirstCar != self):
                self.carColor = self.lastColor
                if(ct.theBestCar != None):
                    if(self.distanceFromGoal < ct.theBestCar.distanceFromGoal):
                        self.parent.setEffectNewBestCar()

    def rendeizeCarWhenInPauser(self):
        #Renderizar Carro sem Movimento ou Pausado
        if(self.isWin):
            ct.isWin = True
            self.carRenderized = pygame.draw.circle(self.windows,(255,255,255),self.pos,ct.scaleCar)
        else:
            self.carRenderized = pygame.draw.circle(self.windows,(0,0,0),self.pos,ct.scaleCar)

    def checkDirection(self):
        #Verificar Colisão com Item de Direção
        id = ct.mapId[self.pos]
        x,y = self.pos
        if(id== 6):
            x = self.pos[0] + 1
            self.pos = (x,y)
            return True
    
        if(id == 7):
            x = self.pos[0] - 1
            self.pos = (x,y)
            return True
        
        if(id == 8):
            y = self.pos[1] -1
            self.pos = (x,y)
            return True

        if(id == 9):
            y = self.pos[1] +1
            self.pos = (x,y)
            return True
        
        return False

    def move(self):
        #Move Carro
        if(self.crashCar == True):
            self.rendeizeCarWhenInPauser()
            return
    
        self.checkSpeed()

        isMoved = False
        for ss in range(self.speedInit):
            if(self.checkCrash()):
                return
            
            self.checkPosition()
            self.neuronController.getNewDirection(self.HelpFromTop, self.HelpFromBottom, self.HelpFromLeft, self.HelpFromRight,self.speedInit,self.HelpFromRightTop, self.HelpFromRightBottom, self.HelpFromLeftTop, self.HelpFromLeftBottom) 

            self.checkDistanceFromGoal()
            
            
            x = self.pos[0]
            y = self.pos[1]
            
            if(self.checkDirection() == False):
                if (self.neuronController.neuroFoward.valueFinal > self.valueActivetion):
                    y = self.pos[1] - 1
                    isMoved = True
                if self.neuronController.neuroBack.valueFinal > self.valueActivetion:
                    y = self.pos[1] + 1
                    isMoved = True
                if self.neuronController.neuroTurnLeft.valueFinal > self.valueActivetion:
                    x = self.pos[0] - 1
                    isMoved = True
                if self.neuronController.neuroTurnRight.valueFinal > self.valueActivetion:
                    x = self.pos[0] + 1 
                    isMoved = True

                self.pos = (x,y)
                if(self.pos in self.listPosWalked):  
                    self.crashCar = True
            else:
                isMoved = True
                
            if self.neuronController.neuroSpeed.valueFinal > self.valueActivetion and self.speedInit < 15:
                self.speedInit += 1
            if self.neuronController.neuroSpeed.valueFinal < self.valueActivetion and self.speedInit > 10:
                self.speedInit -= 1   

            self.listPosWalked.append(self.pos)
            self.carRenderized = pygame.draw.circle(self.windows,self.carColor,self.pos, ct.scaleCar)

        if(isMoved):
            self.countLimitStop = 0
        else:
            self.countLimitStop += 1 

        if(self.countLimitStop > 50):
              self.crashCar = True    
           

#Guarda as Distancias e os Itens Colidos para cada Sensor   
class HelpCheckDistanceAndObjectCollider():
    def __init__(self) -> None:
        #Construtor
        self.resetCheck()
        pass

    def resetCheck(self):
        #Restaura Valores
        self.disCount = 0
        self.itemMemory = 0
        self.idItemCollider = -1
        self.distaceFromCollider = -1

    def updateValue(self,itemCollider):
        #Salva Valores
        self.idItemCollider = itemCollider
        self.itemMemory = itemCollider
        self.distaceFromCollider = self.disCount
        