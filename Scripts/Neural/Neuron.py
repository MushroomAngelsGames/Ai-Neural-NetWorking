import random as rd
import Interface.Constants as ct

#Gerar Valor Aleatorio.
def getRandoValue(valueLimit = 2000):
    return (rd.uniform(-valueLimit,valueLimit))

#Controlador de Pesos das camadas Ocultas
class Weights():
    def __init__(self,isFirst,betterWeights = None,isWin = False) -> None:
        #Inicializar Pesos
        self.bias = []
        self.weights = []

        if(isWin):
            for ss in betterWeights.weights:
                self.weights.append(ss)

            for ss in betterWeights.bias:
                self.bias.append(ss)

            return

        if isFirst == False or betterWeights == None:
            for ss in range(9):
                self.weights.append(getRandoValue(1))
                self.bias.append(getRandoValue(1))

        else:
            valueWeights = ct.mutationFactor*1000

            for ss in betterWeights.weights:
                self.weights.append(ss + getRandoValue(valueWeights))

            for ss in betterWeights.bias:
                if(ct.typeBias != 2):
                    self.bias.append((ss + getRandoValue(valueWeights)) if (ct.typeBias == 0) else ss)
                else:
                    self.bias.append(1)

        pass

    def update(self):
        valueWeights = ct.mutationFactor*1000

        index = 0
        for ss in self.weights:
            self.weights[index] = self.weights[index] + getRandoValue(valueWeights)
            index += 1

        index = 0
        for ss in self.bias:
            if(ct.typeBias != 2):
                self.bias[index] = (self.bias[index]  + getRandoValue(valueWeights)) if (ct.typeBias == 0) else self.bias[index] 
                index +=1 

#Controlador de Peso da Camada de Saída
class WeightsLeave():
    def __init__(self,isFirst,betterWeights = None,isWin = False) -> None:
        #Inicializar Pesos
        self.bias = []
        self.weights = []
   
        if(isWin):
            for ss in betterWeights.weights:
                self.weights.append(ss)

            for ss in betterWeights.bias:
                self.bias.append(ss)

            return

        if isFirst == False or betterWeights == None:
            for ss in range(6):  
                self.weights.append(getRandoValue(1))
                self.bias.append(getRandoValue(1))


        else:
            valueWeights = ct.mutationFactor*1000

            for ss in betterWeights.weights:
                self.weights.append(ss + getRandoValue(valueWeights))

            for ss in betterWeights.bias:
                if(ct.typeBias != 2):
                    self.bias.append((ss + getRandoValue(valueWeights)) if (ct.typeBias == 0) else ss)
                else:
                    self.bias.append(1)      
        pass

    def update(self):
        valueWeights = ct.mutationFactor*1000

        index = 0
        for ss in self.weights:
            self.weights[index] = self.weights[index] + getRandoValue(valueWeights)
            index += 1
       

        index = 0
        for ss in self.bias:
            if(ct.typeBias != 2):
                self.bias[index] = (self.bias[index]  + getRandoValue(valueWeights)) if (ct.typeBias == 0) else self.bias[index] 
                index +=1 

#Controlador Cerebro dos Carros
class NeuronController():
    def __init__(self,BetterWeights = None) -> None:
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

        isNone = True
        if(BetterWeights.isWithValues):
            isNone = False

        self.weights1Neuron1 = Weights(BetterWeights.isWithValues,None if isNone else weights[0],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weights1Neuron2 = Weights(BetterWeights.isWithValues,None if isNone else weights[1],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weights1Neuron3 = Weights(BetterWeights.isWithValues,None if isNone else weights[2],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weights1Neuron4 = Weights(BetterWeights.isWithValues,None if isNone else weights[3],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weights1Neuron5 = Weights(BetterWeights.isWithValues,None if isNone else weights[4],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weights1Neuron6 = Weights(BetterWeights.isWithValues,None if isNone else weights[5],ct.theBestCar.isWin if ct.theBestCar!= None else False)

        self.weights1Neuron1_layer2 = WeightsLeave(BetterWeights.isWithValues,None if isNone else weightsLayer2[0],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weights1Neuron2_layer2 = WeightsLeave(BetterWeights.isWithValues,None if isNone else weightsLayer2[1],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weights1Neuron3_layer2 = WeightsLeave(BetterWeights.isWithValues,None if isNone else weightsLayer2[2],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weights1Neuron4_layer2 = WeightsLeave(BetterWeights.isWithValues,None if isNone else weightsLayer2[3],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weights1Neuron5_layer2 = WeightsLeave(BetterWeights.isWithValues,None if isNone else weightsLayer2[4],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weights1Neuron6_layer2 = WeightsLeave(BetterWeights.isWithValues,None if isNone else weightsLayer2[5],ct.theBestCar.isWin if ct.theBestCar!= None else False)

        self.weights1Neuron1_layer3 = WeightsLeave(BetterWeights.isWithValues,None if isNone else weightsLayer3[0],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weights1Neuron2_layer3 = WeightsLeave(BetterWeights.isWithValues,None if isNone else weightsLayer3[1],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weights1Neuron3_layer3 = WeightsLeave(BetterWeights.isWithValues,None if isNone else weightsLayer3[2],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weights1Neuron4_layer3 = WeightsLeave(BetterWeights.isWithValues,None if isNone else weightsLayer3[3],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weights1Neuron5_layer3 = WeightsLeave(BetterWeights.isWithValues,None if isNone else weightsLayer3[4],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weights1Neuron6_layer3 = WeightsLeave(BetterWeights.isWithValues,None if isNone else weightsLayer3[5],ct.theBestCar.isWin if ct.theBestCar!= None else False)

        self.weightsLeaveFoward = WeightsLeave(BetterWeights.isWithValues,None if isNone else weightsLeave[0],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weightsLeaveBottom = WeightsLeave(BetterWeights.isWithValues,None if isNone else weightsLeave[1],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weightsLeaveLeft = WeightsLeave(BetterWeights.isWithValues,None if isNone else weightsLeave[2],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weightsLeaveRight = WeightsLeave(BetterWeights.isWithValues,None if isNone else weightsLeave[3],ct.theBestCar.isWin if ct.theBestCar!= None else False)
        self.weightsSpeed = WeightsLeave(BetterWeights.isWithValues,None if isNone else weightsLeave[4],ct.theBestCar.isWin if ct.theBestCar!= None else False)
       
        pass

    def update(self):
        self.weights1Neuron1.update()
        self.weights1Neuron2.update()
        self.weights1Neuron3.update()
        self.weights1Neuron4.update()
        self.weights1Neuron5.update()
        self.weights1Neuron6.update()

        if(ct.typeCamadas != 1):
            self.weights1Neuron1_layer2.update()
            self.weights1Neuron2_layer2.update()
            self.weights1Neuron3_layer2.update()
            self.weights1Neuron4_layer2.update()
            self.weights1Neuron5_layer2.update()
            self.weights1Neuron6_layer2.update()

            self.weights1Neuron1_layer3.update()
            self.weights1Neuron2_layer3.update()
            self.weights1Neuron3_layer3.update()
            self.weights1Neuron4_layer3.update()
            self.weights1Neuron5_layer3.update()
            self.weights1Neuron6_layer3.update()

        self.weightsLeaveFoward.update()
        self.weightsLeaveBottom.update()
        self.weightsLeaveLeft.update()
        self.weightsLeaveRight.update()
        self.weightsSpeed.update()


    def getNewDirection(self,HelpFromTop,HelpFromBottom,HelpFromLeft,HelpFromRight,speed,HelpFromTopRight,HelpFromBottomRight,HelpFromTopLeft,HelpFromBottomLeft):
        #Gerar Novos Valores

        self.neuro1 = Neuron(HelpFromTop,HelpFromBottom,HelpFromLeft,HelpFromRight,speed,HelpFromTopRight,HelpFromBottomRight,HelpFromTopLeft,HelpFromBottomLeft,self.weights1Neuron1)
        self.neuro2 = Neuron(HelpFromTop,HelpFromBottom,HelpFromLeft,HelpFromRight,speed,HelpFromTopRight,HelpFromBottomRight,HelpFromTopLeft,HelpFromBottomLeft,self.weights1Neuron2)
        self.neuro3 = Neuron(HelpFromTop,HelpFromBottom,HelpFromLeft,HelpFromRight,speed,HelpFromTopRight,HelpFromBottomRight,HelpFromTopLeft,HelpFromBottomLeft,self.weights1Neuron3)
        self.neuro4 = Neuron(HelpFromTop,HelpFromBottom,HelpFromLeft,HelpFromRight,speed,HelpFromTopRight,HelpFromBottomRight,HelpFromTopLeft,HelpFromBottomLeft,self.weights1Neuron4)
        self.neuro5 = Neuron(HelpFromTop,HelpFromBottom,HelpFromLeft,HelpFromRight,speed,HelpFromTopRight,HelpFromBottomRight,HelpFromTopLeft,HelpFromBottomLeft,self.weights1Neuron5)
        self.neuro6 = Neuron(HelpFromTop,HelpFromBottom,HelpFromLeft,HelpFromRight,speed,HelpFromTopRight,HelpFromBottomRight,HelpFromTopLeft,HelpFromBottomLeft,self.weights1Neuron6)

        #1 Camada oculta
        if(ct.typeCamadas == 1):
            self.neuroFoward = NeuronLeave(self.neuro1,self.neuro2,self.neuro3,self.neuro4,self.neuro5,self.neuro6,self.weightsLeaveFoward,theFinal= True)
            self.neuroBack = NeuronLeave(self.neuro1,self.neuro2,self.neuro3,self.neuro4,self.neuro5,self.neuro6,self.weightsLeaveBottom,theFinal= True)
            self.neuroTurnLeft = NeuronLeave(self.neuro1,self.neuro2,self.neuro3,self.neuro4,self.neuro5,self.neuro6,self.weightsLeaveLeft,theFinal= True)
            self.neuroTurnRight = NeuronLeave(self.neuro1,self.neuro2,self.neuro3,self.neuro4,self.neuro5,self.neuro6,self.weightsLeaveRight,theFinal= True)
            self.neuroSpeed = NeuronLeave(self.neuro1,self.neuro2,self.neuro3,self.neuro4,self.neuro5,self.neuro6,self.weightsSpeed,theFinal= True)

        if(ct.typeCamadas != 1):
            self.neuro1_layer2 = NeuronLeave(self.neuro1,self.neuro2,self.neuro3,self.neuro4,self.neuro5,self.neuro6,self.weights1Neuron1_layer2)
            self.neuro2_layer2 = NeuronLeave(self.neuro1,self.neuro2,self.neuro3,self.neuro4,self.neuro5,self.neuro6,self.weights1Neuron2_layer2)
            self.neuro3_layer2 = NeuronLeave(self.neuro1,self.neuro2,self.neuro3,self.neuro4,self.neuro5,self.neuro6,self.weights1Neuron3_layer2)
            self.neuro4_layer2 = NeuronLeave(self.neuro1,self.neuro2,self.neuro3,self.neuro4,self.neuro5,self.neuro6,self.weights1Neuron4_layer2)
            self.neuro5_layer2 = NeuronLeave(self.neuro1,self.neuro2,self.neuro3,self.neuro4,self.neuro5,self.neuro6,self.weights1Neuron5_layer2)
            self.neuro6_layer2 = NeuronLeave(self.neuro1,self.neuro2,self.neuro3,self.neuro4,self.neuro5,self.neuro6,self.weights1Neuron6_layer2)

        #2 Camada oculta
        if(ct.typeCamadas == 2):
            self.neuroFoward = NeuronLeave(self.neuro1_layer2,self.neuro2_layer2,self.neuro3_layer2,self.neuro4_layer2,self.neuro5_layer2,self.neuro6_layer2,self.weightsLeaveFoward,theFinal= True)
            self.neuroBack = NeuronLeave(self.neuro1_layer2,self.neuro2_layer2,self.neuro3_layer2,self.neuro4_layer2,self.neuro5_layer2,self.neuro6_layer2,self.weightsLeaveBottom,theFinal= True)
            self.neuroTurnLeft = NeuronLeave(self.neuro1_layer2,self.neuro2_layer2,self.neuro3_layer2,self.neuro4_layer2,self.neuro5_layer2,self.neuro6_layer2,self.weightsLeaveLeft,theFinal= True)
            self.neuroTurnRight = NeuronLeave(self.neuro1_layer2,self.neuro2_layer2,self.neuro3_layer2,self.neuro4_layer2,self.neuro5_layer2,self.neuro6_layer2,self.weightsLeaveRight,theFinal= True)
            self.neuroSpeed = NeuronLeave(self.neuro1_layer2,self.neuro2_layer2,self.neuro3_layer2,self.neuro4_layer2,self.neuro5_layer2,self.neuro6_layer2,self.weightsSpeed,theFinal= True)

        #3 Camadas Ocultas
        if(ct.typeCamadas == 3):
            self.neuro1_layer3 = NeuronLeave(self.neuro1_layer2,self.neuro2_layer2,self.neuro3_layer2,self.neuro4_layer2,self.neuro5_layer2,self.neuro6_layer2,self.weights1Neuron1_layer3)
            self.neuro2_layer3 = NeuronLeave(self.neuro1_layer2,self.neuro2_layer2,self.neuro3_layer2,self.neuro4_layer2,self.neuro5_layer2,self.neuro6_layer2,self.weights1Neuron2_layer3)
            self.neuro3_layer3 = NeuronLeave(self.neuro1_layer2,self.neuro2_layer2,self.neuro3_layer2,self.neuro4_layer2,self.neuro5_layer2,self.neuro6_layer2,self.weights1Neuron3_layer3)
            self.neuro4_layer3 = NeuronLeave(self.neuro1_layer2,self.neuro2_layer2,self.neuro3_layer2,self.neuro4_layer2,self.neuro5_layer2,self.neuro6_layer2,self.weights1Neuron4_layer3)
            self.neuro5_layer3 = NeuronLeave(self.neuro1_layer2,self.neuro2_layer2,self.neuro3_layer2,self.neuro4_layer2,self.neuro5_layer2,self.neuro6_layer2,self.weights1Neuron5_layer3)
            self.neuro6_layer3 = NeuronLeave(self.neuro1_layer2,self.neuro2_layer2,self.neuro3_layer2,self.neuro4_layer2,self.neuro5_layer2,self.neuro6_layer2,self.weights1Neuron6_layer3)

            self.neuroFoward = NeuronLeave(self.neuro1_layer3,self.neuro2_layer3,self.neuro3_layer3,self.neuro4_layer3,self.neuro5_layer3,self.neuro6_layer3,self.weightsLeaveFoward,theFinal= True)
            self.neuroBack = NeuronLeave(self.neuro1_layer3,self.neuro2_layer3,self.neuro3_layer3,self.neuro4_layer3,self.neuro5_layer3,self.neuro6_layer3,self.weightsLeaveBottom,theFinal= True)
            self.neuroTurnLeft = NeuronLeave(self.neuro1_layer3,self.neuro2_layer3,self.neuro3_layer3,self.neuro4_layer3,self.neuro5_layer3,self.neuro6_layer3,self.weightsLeaveLeft,theFinal= True)
            self.neuroTurnRight = NeuronLeave(self.neuro1_layer3,self.neuro2_layer3,self.neuro3_layer3,self.neuro4_layer3,self.neuro5_layer3,self.neuro6_layer3,self.weightsLeaveRight,theFinal= True)
            self.neuroSpeed = NeuronLeave(self.neuro1_layer3,self.neuro2_layer3,self.neuro3_layer3,self.neuro4_layer3,self.neuro5_layer3,self.neuro6_layer3,self.weightsSpeed,theFinal= True)

#Neuronio da Camada de Saída
class NeuronLeave():
    def __init__(self,neuronValue1,neuronValue2,neuronValue3,neuronValue4,neuronValue5,neuronValue6,weights,theFinal = False) -> None:
        #Inicializar Neuronio
        self.valueFinal = 0
        self.listWithValeuFromNeurom = []
        self.listWithValeuFromNeurom.append(neuronValue1.valueFinal)
        self.listWithValeuFromNeurom.append(neuronValue2.valueFinal)
        self.listWithValeuFromNeurom.append(neuronValue3.valueFinal)
        self.listWithValeuFromNeurom.append(neuronValue4.valueFinal)
        self.listWithValeuFromNeurom.append(neuronValue5.valueFinal)
        self.listWithValeuFromNeurom.append(neuronValue6.valueFinal)
        self.theFinal = theFinal
        self.allWeights = weights
        self.multiplyWeights()
        self.sumValues()
        pass

    def multiplyWeights(self):
        #Multiplicar Valores
        index = 0
        for ss in self.listWithValeuFromNeurom:         
            self.listWithValeuFromNeurom[index] = ss *  self.allWeights.weights[index] * self.allWeights.bias[index]
            index += 1 


    def sumValues(self):
        #Somar Valores
        for ss in self.listWithValeuFromNeurom:
            self.valueFinal += ss 
           
        self.relu()
   
    def relu(self):   
        #Função de Ativaçao 
       
        if(self.valueFinal <= 0):
            self.valueFinal = 0
        else:
            if(self.theFinal):
                self.valueFinal = 2

#Neuronio Camada Oculta 
class Neuron():
    def __init__(self,HelpFromTop,HelpFromBottom,HelpFromLeft,HelpFromRight,speed,HelpFromTopRight,HelpFromBottomRight,HelpFromTopLeft,HelpFromBottomLeft,weights) -> None:
        #Inicializar Neuronio
        self.listWithHelpDistance = []
        self.listWithHelpDistance.append(HelpFromTopRight)
        self.listWithHelpDistance.append(HelpFromBottomRight)
        self.listWithHelpDistance.append(HelpFromTopLeft)
        self.listWithHelpDistance.append(HelpFromBottomLeft)
        self.listWithHelpDistance.append(HelpFromTop)
        self.listWithHelpDistance.append(HelpFromBottom)
        self.listWithHelpDistance.append(HelpFromLeft)
        self.listWithHelpDistance.append(HelpFromRight)
        self.speed = speed
        self.classWeights = weights
        self.valueFinal = 0
        self.valueHelpInterface = 0
        self.multiplyWeights()
        self.sumValues()
        pass

    def multiplyWeights(self):
        #Multiplicar Valores
        index = 0
        for ss in self.listWithHelpDistance:
            self.listWithHelpDistance[index].distaceFromCollider =  ss.idItemCollider +  ss.distaceFromCollider  * self.classWeights.weights[index] *  self.classWeights.bias[index]
            index +=1

        self.speed = self.speed * self.classWeights.weights[8] *  self.classWeights.bias[8]

    def sumValues(self):
        #Somar Valores
        for ss in self.listWithHelpDistance:
             self.valueFinal += ss.distaceFromCollider 

        self.valueFinal += self.speed 

        self.relu()
  
    def relu(self):
        #Função de Ativaçao
        if(self.valueFinal < 0):
            self.valueFinal = 0
            self.valueHelpInterface = 0
        else:
            self.valueHelpInterface = 1

       