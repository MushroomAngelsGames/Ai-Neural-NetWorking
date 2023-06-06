import Objects.ItemBuildClass as item
import pygame

#Nome do Software
nameGameForNameWindow = "Traffic Neural Network"
nameCancelBuild ="Clique no [ MOUSE 1] Para Cancelar Construção"
labelBrush ="Aumentar Rua Tecla [1]    ||    Diminuir Rua => Tecla [2]"
#Variaveis
menuFont = None 
fps = 60

#Tamanho da Tela
menuHeight =  640
menuWidth  = 480
gameHeight =  980
gameWidth  = 1720

#Em Runtime
inGame = False
countTimeLimit = 0
countTimeLimitAll = 0
generation = 1

#Local das Imagens Usadas no Jogo
dicImageBut = ".\Imagens\Interface\But.png"
dicImageBut1 = ".\Imagens\Interface\But2.png"
dicImageBut2 = ".\Imagens\Interface\But3.png"
dicBackGroundImageMenu1 = ".\Imagens\Interface\BackGround1.png"
dicBackGroundImageMenu2 = ".\Imagens\Interface\BackGround2.png"
dicBackGroundImageMenu5 = ".\Imagens\Interface\BackGround3.png"
dicBackGroundImageRoad = ".\Imagens\Interface\spriteRoad.png"
dicBackGroundImageMenu = ".\Imagens\Interface\menu1.png"
dicBackGroundImageMenu3 = ".\Imagens\Interface\menu2.png"
dicBackGroundImageMenu3 = ".\Imagens\Interface\menu3.png"
dicBackGroundImageMenu4 = ".\Imagens\Interface\menuDescription.png"

maxPopulationInOnTime = 15
timeLimit = 1000
population = 2000
scaleCar = 10
halfscaleCar = 5
carColorBetter = (0,255,0)
disTheBestCarInGeneration = 0
isWin = False

#Melhor Veiculo
theBestCar = None
theFirstCar = None
theBest = 500000000000000
countFinish = 1
mutationFactor = 0.05
typeCamadas = 1

#Posição dos Itens no Mapa.
mapId = {}
mapIdDistaceFromEnd = {}


#Lista de Itens Construidos.
scenaryAll = []
scenaryRoad = []


#Configurar Ponto de Inicio e Chegada.
StartPos = None
FinalPos = None
centerFinalPos = None
idStart = None
idFinal = None

sizeRoad = (100,100)
#Castrar os Objetos que serão Usados na Construção do Cenario
limite =  item.ItemBuildClass(0,".\Imagens\ItemBuild/Pincel.png","Rua","Use Esse Item para desenhar as ruas",(100,100),0,True)
itemBuild = [
    limite,
    item.ItemBuildClass(1,".\Imagens\ItemBuild/burraco.png","Burraco", "É um Obstaculo",(35,35),1,False),
    item.ItemBuildClass(2,".\Imagens\ItemBuild/Start.png","Início", "É o Ponto Inicial da Rede Neural",(75,75),2,False),
    item.ItemBuildClass(3,".\Imagens\ItemBuild/Chegada.png","Chegada", "É o Objetivo da Rede Neural",(75,75),3,False),
    item.ItemBuildClass(4,".\Imagens\ItemBuild/Speed.png","Speed", "Aumenta a Velocidade do Carro",(35,35),4,False),
    item.ItemBuildClass(5,".\Imagens\ItemBuild/Tree.png","Arvore", "É um Obstaculo",(35,35),1,False),
    item.ItemBuildClass(6,".\Imagens\ItemBuild/slowly.png","Slowly", "Diminui a Velocidade do Carro",(35,35),5,False),
    item.ItemBuildClass(7,".\Imagens\ItemBuild/direita.png","Right", "Força o Carro a Virar a Direita",(35,35),6,False),
    item.ItemBuildClass(8,".\Imagens\ItemBuild/esquerda.png","Left", "Força o Carro a Virar a Esquerda",(35,35),7,False),
    item.ItemBuildClass(9,".\Imagens\ItemBuild/subir.png","Up", "Força o Carro a Subir",(35,35),8,False),
    item.ItemBuildClass(10,".\Imagens\ItemBuild/descer.png","Down", "Força o Carro a Descer",(35,35),9,False),
    ]

def initBoard():
   limite.itemIcone = pygame.transform.scale(limite.itemIcone, limite.size)
  

