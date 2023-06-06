import random as rd
import Interface.Constants as ct
import math

#Gerar Valor Aleatorio.
def getRandoValue(valueLimit = 2000):
    return (rd.uniform(-valueLimit,valueLimit))

#Controlador de Pesos das camadas Ocultas
class Weights():
    def __init__(self,isFirst,betterWeights = None,isWin = False) -> None:
        #Inicializar Pesos
        self.weightsDisTop =0
        self.weightsDisBottom =0
        self.weightsDisLeft =0
        self.weightsDisRight =0    
        self.weightSpeed =0

        self.weightsDisTopRight =0
        self.weightsDisBottomRight =0
        self.weightsDisTopLeft =0
        self.weightsDisBottomLeft =0
    
        self.bias = []

        if(isWin):
            self.weightsDisTop += betterWeights.weightsDisTop
            self.weightsDisBottom+=betterWeights.weightsDisBottom
            self.weightsDisLeft +=betterWeights.weightsDisLeft
            self.weightsDisRight +=betterWeights.weightsDisRight
            self.weightSpeed += betterWeights.weightSpeed

            self.weightsDisTopRight +=betterWeights.weightsDisTopRight
            self.weightsDisBottomRight += betterWeights.weightsDisBottomRight
            self.weightsDisTopLeft +=betterWeights.weightsDisTopLeft
            self.weightsDisBottomLeft +=betterWeights.weightsDisBottomLeft
            
            for ss in range(self.bias):
                self.bias.append(betterWeights.bias[ss])

            return

        typeCar = rd.randint(1,20) if isFirst == False else 0
        if typeCar == 0:
            self.weightsDisTop += getRandoValue(1)
            self.weightsDisBottom += getRandoValue(1)
            self.weightsDisLeft += getRandoValue(1)
            self.weightsDisRight += getRandoValue(1)
            self.weightSpeed += getRandoValue(1)

            self.weightsDisTopRight += getRandoValue(1)
            self.weightsDisBottomRight += getRandoValue(1)
            self.weightsDisTopLeft += getRandoValue(1)
            self.weightsDisBottomLeft += getRandoValue(1)
            
            for ss in range(9):
                self.bias.append(getRandoValue(1))

        elif typeCar > 1 and typeCar <=12:
            valueWeights = ct.mutationFactor*ct.theBest

            self.weightsDisTop += betterWeights.weightsDisTop + getRandoValue(valueWeights)
            self.weightsDisBottom +=betterWeights.weightsDisBottom  + getRandoValue(valueWeights)
            self.weightsDisLeft +=betterWeights.weightsDisLeft + getRandoValue(valueWeights)
            self.weightsDisRight +=betterWeights.weightsDisRight + getRandoValue(valueWeights)
            self.weightSpeed += betterWeights.weightSpeed + getRandoValue(valueWeights)

            self.weightsDisTopRight +=betterWeights.weightsDisTopRight + getRandoValue(valueWeights)
            self.weightsDisBottomRight += betterWeights.weightsDisBottomRight + getRandoValue(valueWeights)
            self.weightsDisTopLeft +=betterWeights.weightsDisTopLeft + getRandoValue(valueWeights)
            self.weightsDisBottomLeft +=betterWeights.weightsDisBottomLeft + getRandoValue(valueWeights)
           

            for ss in betterWeights.bias:
                self.bias.append(ss + getRandoValue(valueWeights))

        else:
            valueWeights = 10

            self.weightsDisTop += betterWeights.weightsDisTop + getRandoValue(valueWeights)
            self.weightsDisBottom +=betterWeights.weightsDisBottom  + getRandoValue(valueWeights)
            self.weightsDisLeft +=betterWeights.weightsDisLeft + getRandoValue(valueWeights)
            self.weightsDisRight +=betterWeights.weightsDisRight + getRandoValue(valueWeights)
            self.weightSpeed += betterWeights.weightSpeed + getRandoValue(valueWeights)

            self.weightsDisTopRight +=betterWeights.weightsDisTopRight  + getRandoValue(valueWeights)
            self.weightsDisBottomRight += betterWeights.weightsDisBottomRight  + getRandoValue(valueWeights)
            self.weightsDisTopLeft +=betterWeights.weightsDisTopLeft  + getRandoValue(valueWeights)
            self.weightsDisBottomLeft +=betterWeights.weightsDisBottomLeft  + getRandoValue(valueWeights)

            for ss in betterWeights.bias:
                self.bias.append(ss + getRandoValue(valueWeights))

        pass

#Controlador de Peso da Camada de Saída
class WeightsLeave():
    def __init__(self,car,betterWeights = None,isWin = False) -> None:
        #Inicializar Pesos
        self.leave1 =0
        self.leave2 =0
        self.leave3 =0
        self.leave4 =0
        self.leave5 =0
        self.leave6 =0
        self.bias = []
        typeCar = rd.randint(1,20) if car.isFirst == False else 0

        if typeCar == 0:
            self.leave1 += getRandoValue(1)
            self.leave2 += getRandoValue(1)
            self.leave3 += getRandoValue(1)
            self.leave4 += getRandoValue(1)
            self.leave5 += getRandoValue(1)
            self.leave6 += getRandoValue(1)

                
            for ss in range(6):
                self.bias.append(getRandoValue(1))

        elif typeCar > 1 and typeCar <=13:
            valueWeights = ct.mutationFactor*ct.theBest
            self.leave1 += betterWeights.leave1 + getRandoValue(valueWeights)
            self.leave2 += betterWeights.leave2 + getRandoValue(valueWeights)
            self.leave3 += betterWeights.leave3 + getRandoValue(valueWeights)
            self.leave4 += betterWeights.leave4 + getRandoValue(valueWeights)
            self.leave5 += betterWeights.leave5 + getRandoValue(valueWeights)
            self.leave6 += betterWeights.leave6 + getRandoValue(valueWeights)

            for ss in betterWeights.bias:
                self.bias.append(ss + getRandoValue(valueWeights))

        else:
            valueWeights = 20 
            self.leave1 += betterWeights.leave1 + getRandoValue(valueWeights)
            self.leave2 += betterWeights.leave2 + getRandoValue(valueWeights)
            self.leave3 += betterWeights.leave3 + getRandoValue(valueWeights)
            self.leave4 += betterWeights.leave4 + getRandoValue(valueWeights)
            self.leave5 += betterWeights.leave5 + getRandoValue(valueWeights)
            self.leave6 += betterWeights.leave6 + getRandoValue(valueWeights)

            for ss in betterWeights.bias:
                self.bias.append(ss + getRandoValue(valueWeights))
                
        pass

#Controlador Cerebro dos Carros
class NeuronController():
    def __init__(self,car,BetterWeights = None) -> None:
        #Inicializar Cerebro
        self.neuro1 = None
        self.neuro2 = None
        self.neuro3 = None
        self.neuro4 = None
        self.neuro5 = None
        self.neuro6 = None

        self.neuro1_layer2 = None
        self.neuro2_layer2 = None
        self.neuro3_layer2 = None
        self.neuro4_layer2 = None
        self.neuro5_layer2 = None
        self.neuro6_layer2 = None  

        self.neuro1_layer3 = None
        self.neuro2_layer3 = None
        self.neuro3_layer3 = None
        self.neuro4_layer3 = None
        self.neuro5_layer3 = None
        self.neuro6_layer3 = None  

        self.neuroFoward = None
        self.neuroBack = None
        self.neuroTurnLeft = None
        self.neuroTurnRight = None
        self.neuroSpeed = None

        weightsLeave = BetterWeights.getListDirectionsWeights()
        weights = BetterWeights.getListLeaveWeights()
        weightsLayer2 = BetterWeights.getListLeaveWeights_layer2()
        weightsLayer3 = BetterWeights.getListLeaveWeights_layer3()

        self.weights1Neuron1 = Weights(car.isFirst,None if car.isFirst else weights[0],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weights1Neuron2 = Weights(car.isFirst,None if car.isFirst else weights[1],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weights1Neuron3 = Weights(car.isFirst,None if car.isFirst else weights[2],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weights1Neuron4 = Weights(car.isFirst,None if car.isFirst else weights[3],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weights1Neuron5 = Weights(car.isFirst,None if car.isFirst else weights[4],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weights1Neuron6 = Weights(car.isFirst,None if car.isFirst else weights[5],ct.theBestCar.isWin if ct.theBestCar!= None else False)

        self.weights1Neuron1_layer2 = WeightsLeave(car,None if car.isFirst else weightsLayer2[0],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weights1Neuron2_layer2 = WeightsLeave(car,None if car.isFirst else weightsLayer2[1],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weights1Neuron3_layer2 = WeightsLeave(car,None if car.isFirst else weightsLayer2[2],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weights1Neuron4_layer2 = WeightsLeave(car,None if car.isFirst else weightsLayer2[3],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weights1Neuron5_layer2 = WeightsLeave(car,None if car.isFirst else weightsLayer2[4],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weights1Neuron6_layer2 = WeightsLeave(car,None if car.isFirst else weightsLayer2[5],ct.theBestCar.isWin if ct.theBestCar!= None else False)

        self.weights1Neuron1_layer3 = WeightsLeave(car,None if car.isFirst else weightsLayer3[0],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weights1Neuron2_layer3 = WeightsLeave(car,None if car.isFirst else weightsLayer3[1],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weights1Neuron3_layer3 = WeightsLeave(car,None if car.isFirst else weightsLayer3[2],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weights1Neuron4_layer3 = WeightsLeave(car,None if car.isFirst else weightsLayer3[3],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weights1Neuron5_layer3 = WeightsLeave(car,None if car.isFirst else weightsLayer3[4],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weights1Neuron6_layer3 = WeightsLeave(car,None if car.isFirst else weightsLayer3[5],ct.theBestCar.isWin if ct.theBestCar!= None else False)

        self.weightsLeaveFoward = WeightsLeave(car,None if car.isFirst else weightsLeave[0],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weightsLeaveBottom = WeightsLeave(car,None if car.isFirst else weightsLeave[1],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weightsLeaveLeft = WeightsLeave(car,None if car.isFirst else weightsLeave[2],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weightsLeaveRight = WeightsLeave(car,None if car.isFirst else weightsLeave[3],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weightsSpeed = WeightsLeave(car,None if car.isFirst else weightsLeave[4],ct.theBestCar.isWin if ct.theBestCar!= None else False)
       
        pass

    def getNewDirection(self,HelpFromTop,HelpFromBottom,HelpFromLeft,HelpFromRight,speed,HelpFromTopRight,HelpFromBottomRight,HelpFromTopLeft,HelpFromBottomLeft):
        #Gerar Novos Valores

        self.neuro1 = Neuron(HelpFromTop,HelpFromBottom,HelpFromLeft,HelpFromRight,speed,HelpFromTopRight,HelpFromBottomRight,HelpFromTopLeft,HelpFromBottomLeft,self.weights1Neuron1)
        self.neuro2 = Neuron(HelpFromTop,HelpFromBottom,HelpFromLeft,HelpFromRight,speed,HelpFromTopRight,HelpFromBottomRight,HelpFromTopLeft,HelpFromBottomLeft,self.weights1Neuron2)
        self.neuro3 = Neuron(HelpFromTop,HelpFromBottom,HelpFromLeft,HelpFromRight,speed,HelpFromTopRight,HelpFromBottomRight,HelpFromTopLeft,HelpFromBottomLeft,self.weights1Neuron3)
        self.neuro4 = Neuron(HelpFromTop,HelpFromBottom,HelpFromLeft,HelpFromRight,speed,HelpFromTopRight,HelpFromBottomRight,HelpFromTopLeft,HelpFromBottomLeft,self.weights1Neuron4)
        self.neuro5 = Neuron(HelpFromTop,HelpFromBottom,HelpFromLeft,HelpFromRight,speed,HelpFromTopRight,HelpFromBottomRight,HelpFromTopLeft,HelpFromBottomLeft,self.weights1Neuron5)
        self.neuro6 = Neuron(HelpFromTop,HelpFromBottom,HelpFromLeft,HelpFromRight,speed,HelpFromTopRight,HelpFromBottomRight,HelpFromTopLeft,HelpFromBottomLeft,self.weights1Neuron6)

        self.neuro1_layer2 = NeuronLeave(self.neuro1,self.neuro2,self.neuro3,self.neuro4,self.neuro5,self.neuro6,self.weights1Neuron1_layer2)
        self.neuro2_layer2 = NeuronLeave(self.neuro1,self.neuro2,self.neuro3,self.neuro4,self.neuro5,self.neuro6,self.weights1Neuron2_layer2)
        self.neuro3_layer2 = NeuronLeave(self.neuro1,self.neuro2,self.neuro3,self.neuro4,self.neuro5,self.neuro6,self.weights1Neuron3_layer2)
        self.neuro4_layer2 = NeuronLeave(self.neuro1,self.neuro2,self.neuro3,self.neuro4,self.neuro5,self.neuro6,self.weights1Neuron4_layer2)
        self.neuro5_layer2 = NeuronLeave(self.neuro1,self.neuro2,self.neuro3,self.neuro4,self.neuro5,self.neuro6,self.weights1Neuron5_layer2)
        self.neuro6_layer2 = NeuronLeave(self.neuro1,self.neuro2,self.neuro3,self.neuro4,self.neuro5,self.neuro6,self.weights1Neuron6_layer2)

        self.neuro1_layer3 = NeuronLeave(self.neuro1_layer2,self.neuro2_layer2,self.neuro3_layer2,self.neuro4_layer2,self.neuro5_layer2,self.neuro6_layer2,self.weights1Neuron1_layer3)
        self.neuro2_layer3 = NeuronLeave(self.neuro1_layer2,self.neuro2_layer2,self.neuro3_layer2,self.neuro4_layer2,self.neuro5_layer2,self.neuro6_layer2,self.weights1Neuron2_layer3)
        self.neuro3_layer3 = NeuronLeave(self.neuro1_layer2,self.neuro2_layer2,self.neuro3_layer2,self.neuro4_layer2,self.neuro5_layer2,self.neuro6_layer2,self.weights1Neuron3_layer3)
        self.neuro4_layer3 = NeuronLeave(self.neuro1_layer2,self.neuro2_layer2,self.neuro3_layer2,self.neuro4_layer2,self.neuro5_layer2,self.neuro6_layer2,self.weights1Neuron4_layer3)
        self.neuro5_layer3 = NeuronLeave(self.neuro1_layer2,self.neuro2_layer2,self.neuro3_layer2,self.neuro4_layer2,self.neuro5_layer2,self.neuro6_layer2,self.weights1Neuron5_layer3)
        self.neuro6_layer3 = NeuronLeave(self.neuro1_layer2,self.neuro2_layer2,self.neuro3_layer2,self.neuro4_layer2,self.neuro5_layer2,self.neuro6_layer2,self.weights1Neuron6_layer3)

        #1 Camada oculta
        if(ct.typeCamadas == 1):
            self.neuroFoward = NeuronLeave(self.neuro1,self.neuro2,self.neuro3,self.neuro4,self.neuro5,self.neuro6,self.weightsLeaveFoward)
            self.neuroBack = NeuronLeave(self.neuro1,self.neuro2,self.neuro3,self.neuro4,self.neuro5,self.neuro6,self.weightsLeaveBottom)
            self.neuroTurnLeft = NeuronLeave(self.neuro1,self.neuro2,self.neuro3,self.neuro4,self.neuro5,self.neuro6,self.weightsLeaveLeft)
            self.neuroTurnRight = NeuronLeave(self.neuro1,self.neuro2,self.neuro3,self.neuro4,self.neuro5,self.neuro6,self.weightsLeaveRight)
            self.neuroSpeed = NeuronLeave(self.neuro1,self.neuro2,self.neuro3,self.neuro4,self.neuro5,self.neuro6,self.weightsSpeed)

        #2 Camada oculta
        if(ct.typeCamadas == 2):
            self.neuroFoward = NeuronLeave(self.neuro1_layer2,self.neuro2_layer2,self.neuro3_layer2,self.neuro4_layer2,self.neuro5_layer2,self.neuro6_layer2,self.weightsLeaveFoward)
            self.neuroBack = NeuronLeave(self.neuro1_layer2,self.neuro2_layer2,self.neuro3_layer2,self.neuro4_layer2,self.neuro5_layer2,self.neuro6_layer2,self.weightsLeaveBottom)
            self.neuroTurnLeft = NeuronLeave(self.neuro1_layer2,self.neuro2_layer2,self.neuro3_layer2,self.neuro4_layer2,self.neuro5_layer2,self.neuro6_layer2,self.weightsLeaveLeft)
            self.neuroTurnRight = NeuronLeave(self.neuro1_layer2,self.neuro2_layer2,self.neuro3_layer2,self.neuro4_layer2,self.neuro5_layer2,self.neuro6_layer2,self.weightsLeaveRight)
            self.neuroSpeed = NeuronLeave(self.neuro1_layer2,self.neuro2_layer2,self.neuro3_layer2,self.neuro4_layer2,self.neuro5_layer2,self.neuro6_layer2,self.weightsSpeed)

        #3 Camadas Ocultas
        if(ct.typeCamadas == 3):
            self.neuroFoward = NeuronLeave(self.neuro1_layer3,self.neuro2_layer3,self.neuro3_layer3,self.neuro4_layer3,self.neuro5_layer3,self.neuro6_layer3,self.weightsLeaveFoward)
            self.neuroBack = NeuronLeave(self.neuro1_layer3,self.neuro2_layer3,self.neuro3_layer3,self.neuro4_layer3,self.neuro5_layer3,self.neuro6_layer3,self.weightsLeaveBottom)
            self.neuroTurnLeft = NeuronLeave(self.neuro1_layer3,self.neuro2_layer3,self.neuro3_layer3,self.neuro4_layer3,self.neuro5_layer3,self.neuro6_layer3,self.weightsLeaveLeft)
            self.neuroTurnRight = NeuronLeave(self.neuro1_layer3,self.neuro2_layer3,self.neuro3_layer3,self.neuro4_layer3,self.neuro5_layer3,self.neuro6_layer3,self.weightsLeaveRight)
            self.neuroSpeed = NeuronLeave(self.neuro1_layer3,self.neuro2_layer3,self.neuro3_layer3,self.neuro4_layer3,self.neuro5_layer3,self.neuro6_layer3,self.weightsSpeed)

#Neuronio da Camada de Saída
class NeuronLeave():
    def __init__(self,neuronValue1,neuronValue2,neuronValue3,neuronValue4,neuronValue5,neuronValue6,weights) -> None:
        #Inicializar Neuronio
        self.valueFinal = 0
        self.neuronValue1 = neuronValue1.valueFinal
        self.neuronValue2 = neuronValue2.valueFinal
        self.neuronValue3 = neuronValue3.valueFinal
        self.neuronValue4 = neuronValue4.valueFinal
        self.neuronValue5 = neuronValue5.valueFinal
        self.neuronValue6 = neuronValue6.valueFinal
        self.weights = weights
        self.multiplyWeights()
        self.sumValues()
        pass

    def multiplyWeights(self):
        #Multiplicar Valores
        self.neuronValue1 = self.neuronValue1*self.weights.leave1 + self.weights.bias[0]
        self.neuronValue2 = self.neuronValue2*self.weights.leave2 + self.weights.bias[1]
        self.neuronValue3 = self.neuronValue3*self.weights.leave3 + self.weights.bias[2]
        self.neuronValue4 = self.neuronValue1*self.weights.leave4 + self.weights.bias[3]
        self.neuronValue5 = self.neuronValue2*self.weights.leave5 + self.weights.bias[4]
        self.neuronValue6 = self.neuronValue3*self.weights.leave6 + self.weights.bias[5]

    def sumValues(self):
        #Somar Valores
        self.valueFinal = (self.neuronValue1 + self.neuronValue2 +  self.neuronValue3 + self.neuronValue4 + self.neuronValue5 + self.neuronValue6)
        
        self.relu()
        #self.sigmoid()
        #self.reluInverse()
      
    def reluInverse(self):
        #Função de Ativaçao
        if(self.valueFinal > 0):
            self.valueFinal = 0
        else:
            self.valueFinal = 2

    def relu(self):   
        #Função de Ativaçao 
        if(self.valueFinal < 0):
            self.valueFinal = 0
        else:
            self.valueFinal = 2

    def sigmoid(self):
        #Função de Ativaçao
        self.valueFinal = (1/(1+math.exp(-abs(self.valueFinal))))

        if(self.valueFinal < 0.5):
            self.valueFinal = 0
        else:
            self.valueFinal = 2
  
class Neuron():
    def __init__(self,HelpFromTop,HelpFromBottom,HelpFromLeft,HelpFromRight,speed,HelpFromTopRight,HelpFromBottomRight,HelpFromTopLeft,HelpFromBottomLeft,weights) -> None:
        #Inicializar Neuronio
        self.HelpFromTopRight = HelpFromTopRight
        self.HelpFromBottomRight = HelpFromBottomRight
        self.HelpFromTopLeft = HelpFromTopLeft
        self.HelpFromBottomLeft = HelpFromBottomLeft
        
        self.HelpFromTop = HelpFromTop
        self.HelpFromBottom = HelpFromBottom
        self.HelpFromLeft = HelpFromLeft
        self.HelpFromRight = HelpFromRight
        self.speed = speed

        self.classWeights = weights
        self.valueFinal = 0
        self.valueHelpInterface = 0
        self.multiplyWeights()
        self.sumValues()
        pass

    def multiplyWeights(self):
        #Multiplicar Valores
        self.HelpFromTop.distaceFromCollider = self.HelpFromTop.distaceFromCollider *self.classWeights.weightsDisTop + self.classWeights.bias[0]
        self.HelpFromBottom.distaceFromCollider = self.HelpFromBottom.distaceFromCollider*self.classWeights.weightsDisBottom + self.classWeights.bias[1]
        self.HelpFromLeft.distaceFromCollider  = self.HelpFromLeft.distaceFromCollider*self.classWeights.weightsDisLeft + self.classWeights.bias[2]
        self.HelpFromRight.distaceFromCollider  = self.HelpFromRight.distaceFromCollider*self.classWeights.weightsDisRight + self.classWeights.bias[3]

        self.HelpFromTopRight.distaceFromCollider = self.HelpFromTopRight.distaceFromCollider *self.classWeights.weightsDisTopRight + self.classWeights.bias[4]
        self.HelpFromBottomRight.distaceFromCollider = self.HelpFromBottomRight.distaceFromCollider*self.classWeights.weightsDisBottomRight + self.classWeights.bias[5]
        self.HelpFromTopLeft.distaceFromCollider  = self.HelpFromTopLeft.distaceFromCollider*self.classWeights.weightsDisTopLeft + self.classWeights.bias[6]
        self.HelpFromBottomLeft.distaceFromCollider  = self.HelpFromBottomLeft.distaceFromCollider*self.classWeights.weightsDisBottomLeft + self.classWeights.bias[7]

        self.speed = self.speed*self.classWeights.weightSpeed + self.classWeights.bias[8]
  

    def sumValues(self):
        #Somar Valores
        self.valueFinal = (self.HelpFromTop.distaceFromCollider + self.HelpFromBottom.distaceFromCollider +  self.HelpFromLeft.distaceFromCollider + self.HelpFromRight.distaceFromCollider + self.speed)   
        self.valueFinal += (self.HelpFromTopRight.distaceFromCollider + self.HelpFromBottomRight.distaceFromCollider +  self.HelpFromTopLeft.distaceFromCollider + self.HelpFromBottomLeft.distaceFromCollider)   
       
        self.relu()
        #self.reluInverse()
        #self.sigmoid()

    def sigmoid(self):
        #Função de Ativaçao
        self.valueFinal = (1/(1+math.exp(-abs(self.valueFinal))))

        if(self.valueFinal < 0.5):
            self.valueFinal = 0
            self.valueHelpInterface = 0
        else:
            self.valueHelpInterface = 1

    def reluInverse(self):
        #Função de Ativaçao
        if(self.valueFinal > 0):
            self.valueFinal = 0
            self.valueHelpInterface = 0
        else:
            self.valueHelpInterface = 1       

    def relu(self):
        #Função de Ativaçao
        if(self.valueFinal < 0):
            self.valueFinal = 0
            self.valueHelpInterface = 0
        else:
            self.valueHelpInterface = 1

       