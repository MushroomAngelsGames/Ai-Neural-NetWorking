import Interface.Constants as ct
import CreateMap.MenuInGame as menuInGame
import Neural.car as car 
import pygame
import random as rd

#Class Controle da Rede Neural
class NeuralNetWorking():
    def __init__(self) -> None:
        #Construtor
        self.listCars = []
        self.listCarsDead = []
        self.windows = pygame.display.get_surface()
        self.BetterWeights = ControllerBetterWeights()
  
        self.theFirstGenerarion = True
        self.MenuNeuralInGame = menuInGame.MenuInGame(self)
        ct.generation = 1
        ct.countTimeLimit =0
        self.count =0

        self.effectRestart = pygame.mixer.Sound(".\Music/newGeneration.wav")
        self.effectWin = pygame.mixer.Sound(".\Music/Win.wav")
        self.effectNewBestCar = pygame.mixer.Sound(".\Music/NewBestCar.wav")
        self.effectRestart.set_volume(0.5)
        self.effectWin.set_volume(0.25)
        self.effectNewBestCar.set_volume(0.25)
        self.timeStart =0
        pass

    def createCars(self,amountCars,isFirt = True):
        #Criar Lista de Carros
        if(isFirt):
            self.timeStart = pygame.time.get_ticks()

        self.createCarsWithSetValue(amountCars)
        ct.theFirstCar = self.listCars[0]

    def createCarsWithSetValue(self,amountCars):
        #Criar Lista de Carros no Cenario
        for cars in range(amountCars):   
            self.listCars.append(car.Car(10,(ct.StartPos[0] + rd.randint(0,50),ct.StartPos[1] + rd.randint(0,50)),self))

    def setEffectNewBestCar(self):
         #Efeito Sonoro Quando ha um novo Melhor Carro
        self.effectNewBestCar.play()

    def setEffectWin(self):
        #Efeito Sonoro Quando ganha.
        self.effectWin.play()

    def Restart(self,isFirt=False):
        #Inicializar Nova Geração
        self.listCars.clear()
        self.listCarsDead.clear()
        self.createCars(ct.maxPopulationInOnTime,isFirt)
        ct.countFinish = 1
        ct.generation+=1
        ct.countTimeLimit =0
        ct.theFirstCar = self.listCars[0]
        self.effectRestart.play()

    def resetTheBetter(self):
        self.BetterWeights = ControllerBetterWeights()
        self.Restart()
        ct.theBest = 50000000000000

    def checkInOnlyCar(self,cars):
        #Verificar se o Carro Iformado é o Melhor
        if((((ct.theBest > cars.distanceFromGoal) and cars.isWin == False) or (cars.isWin and ct.theBest > cars.distanceFromGoal))):           
                ct.theBest = cars.distanceFromGoal
                ct.countCheckPoint = cars.countCheckPoint
                ct.theBestCar = cars    
                self.BetterWeights.setNewBetterWeights(cars)

    def checkFinalBestCar(self):     
        #Verificar qual o melhor Carro nas Duas Lista de Carros 
        #for carsLiving in self.listCars:
           #self.checkInOnlyCar(carsLiving)

        for carsDead in self.listCarsDead:
            self.checkInOnlyCar(carsDead)

    def inPauser(self):
        #Pausar Simulação
        self.windows.blit(ct.menuFont.render("SIMULAÇÃO PAUSADA",True,"red"),(ct.gameWidth /2 - 100,ct.gameHeight /2 - 450 )) 
        for cars in self.listCars:
            cars.rendeizeCarWhenInPauser()

        for carsDead in self.listCarsDead:
            carsDead.rendeizeCarWhenInPauser()

    def inRunTime(self):
        #Execultar Simulação
        ct.countTimeLimit += 1 
         
        ct.countTimeLimitAll = (pygame.time.get_ticks() - self.timeStart) / 1000

        for carsDead in self.listCarsDead:
            carsDead.rendeizeCarWhenInPauser()

        for cars in self.listCars:
            cars.move()

        lenCarsDead = len(self.listCarsDead)
        valueListCars = abs(ct.maxPopulationInOnTime - len(self.listCars))


        if((valueListCars < ct.maxPopulationInOnTime and self.BetterWeights.isWithValues) or self.count == ct.maxPopulationInOnTime):
            self.checkFinalBestCar()
            self.createCarsWithSetValue(valueListCars)
            self.count = len(self.listCars) 
          

        if(lenCarsDead >= ct.population or ct.countTimeLimit >= ct.timeLimit):
            self.checkFinalBestCar()
            self.Restart()

        if(self.theFirstGenerarion):
            self.checkFinalBestCar()
            self.Restart(True)
            self.theFirstGenerarion = False

    def update(self):   
            #Definir se Está em RunTime ou Pausado 
            if(ct.inPause == False): 
                self.inRunTime()
            else:
                self.inPauser()

            self.MenuNeuralInGame.update()
            
            
#Amazenar os Pesos do Melhor Carro
class ControllerBetterWeights():
    #Construtor
    def __init__(self) -> None:
        self.isWithValues = False
        self.BetterWeights1Neuron1 = None
        self.BetterWeights1Neuron2 = None
        self.BetterWeights1Neuron3 = None
        self.BetterWeights1Neuron4 = None
        self.BetterWeights1Neuron5 = None
        self.BetterWeights1Neuron6 = None

        self.BetterWeights1Neuron1_layer2 = None
        self.BetterWeights1Neuron2_layer2 = None
        self.BetterWeights1Neuron3_layer2 = None
        self.BetterWeights1Neuron4_layer2 = None
        self.BetterWeights1Neuron5_layer2 = None
        self.BetterWeights1Neuron6_layer2 = None
       
        self.BetterWeights1Neuron1_layer3 = None
        self.BetterWeights1Neuron2_layer3 = None
        self.BetterWeights1Neuron3_layer3 = None
        self.BetterWeights1Neuron4_layer3 = None
        self.BetterWeights1Neuron5_layer3 = None
        self.BetterWeights1Neuron6_layer3 = None

        self.weightsLeaveFoward = None
        self.weightsLeaveBottom = None
        self.weightsLeaveLeft = None
        self.weightsLeaveRight = None
        self.weightsSpeed = None

        pass
    
    #Atribuir Pesos
    def setNewBetterWeights(self,cars):
        self.BetterWeights1Neuron1 = cars.neuronController.weights1Neuron1
        self.BetterWeights1Neuron2 = cars.neuronController.weights1Neuron2
        self.BetterWeights1Neuron3 = cars.neuronController.weights1Neuron3
        self.BetterWeights1Neuron4 = cars.neuronController.weights1Neuron4
        self.BetterWeights1Neuron5 = cars.neuronController.weights1Neuron5
        self.BetterWeights1Neuron6 = cars.neuronController.weights1Neuron6

        self.BetterWeights1Neuron1_layer2 = cars.neuronController.weights1Neuron1_layer2
        self.BetterWeights1Neuron2_layer2 = cars.neuronController.weights1Neuron2_layer2
        self.BetterWeights1Neuron3_layer2 = cars.neuronController.weights1Neuron3_layer2
        self.BetterWeights1Neuron4_layer2 = cars.neuronController.weights1Neuron4_layer2
        self.BetterWeights1Neuron5_layer2 = cars.neuronController.weights1Neuron5_layer2
        self.BetterWeights1Neuron6_layer2 = cars.neuronController.weights1Neuron6_layer2

        self.BetterWeights1Neuron1_layer3 = cars.neuronController.weights1Neuron1_layer3
        self.BetterWeights1Neuron2_layer3 = cars.neuronController.weights1Neuron2_layer3
        self.BetterWeights1Neuron3_layer3 = cars.neuronController.weights1Neuron3_layer3
        self.BetterWeights1Neuron4_layer3 = cars.neuronController.weights1Neuron4_layer3
        self.BetterWeights1Neuron5_layer3 = cars.neuronController.weights1Neuron5_layer3
        self.BetterWeights1Neuron6_layer3 = cars.neuronController.weights1Neuron6_layer3

        self.isWithValues = True
        self.weightsLeaveFoward = cars.neuronController.weightsLeaveFoward
        self.weightsLeaveBottom = cars.neuronController.weightsLeaveBottom
        self.weightsLeaveLeft = cars.neuronController.weightsLeaveLeft
        self.weightsLeaveRight = cars.neuronController.weightsLeaveRight
        self.weightsSpeed = cars.neuronController.weightsSpeed
     
    #Recuperar Lista de Pesos para Neuronios da Nova Geração
    def getListDirectionsWeights(self):
        return  [self.weightsLeaveFoward,self.weightsLeaveBottom, self.weightsLeaveLeft,self.weightsLeaveRight,self.weightsSpeed]
    
    #Recuperar Lista de Pesos para Neuronios da Nova Geração
    def getListLeaveWeights_layer2(self):
        return  [self.BetterWeights1Neuron1_layer2 ,self.BetterWeights1Neuron2_layer2 , self.BetterWeights1Neuron3_layer2 ,
                 self.BetterWeights1Neuron4_layer2 ,self.BetterWeights1Neuron5_layer2 , self.BetterWeights1Neuron6_layer2 ]
    
    #Recuperar Lista de Pesos para Neuronios da Nova Geração
    def getListLeaveWeights_layer3(self):
        return  [self.BetterWeights1Neuron1_layer3 ,self.BetterWeights1Neuron2_layer3 , self.BetterWeights1Neuron3_layer3 ,
                 self.BetterWeights1Neuron4_layer3 ,self.BetterWeights1Neuron5_layer3 , self.BetterWeights1Neuron6_layer3 ]
    
    #Recuperar Lista de Pesos para Neuronios da Nova Geração
    def getListLeaveWeights(self):
        return  [self.BetterWeights1Neuron1,self.BetterWeights1Neuron2, self.BetterWeights1Neuron3,
                 self.BetterWeights1Neuron4,self.BetterWeights1Neuron5, self.BetterWeights1Neuron6]