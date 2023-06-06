import pygame 
import Interface.Constants as ct
import Neural.NeuralNetWorking as nt
import Interface.Button as bt
from pygame.locals import *
import CreateMap.CreateMapMenuBuild as ctMapMenuBuild
import CreateMap.MenuBrush as brush

#Controlador Geral dos Menus
class CreateMapMenu():
    def __init__(self) -> None:
        #Construtor
        self.windows = pygame.display.get_surface()
        self.stateBuild = True
        self.inGame = False
        self.inBuild = False
        self.useGrid = False
        self.itemBuildController = None
        ct.initBoard()
        self.NeuralNetWorking = nt.NeuralNetWorking()
        self.createMapId()
        pass

    def createInteractionGrild(self):
        #Criar Grid 
        valueGrild = 95
        distanceRowns = ct.gameWidth // valueGrild
        x = 0
        y = 0
        for l in range(valueGrild):
            x += distanceRowns
            y += distanceRowns
            pygame.draw.line(self.windows,(0,0,0),(x,0),(x,ct.gameWidth))
            pygame.draw.line(self.windows,(0,0,0),(0,y),(ct.gameWidth,y))

    def controllerButs(self):
        #Atualizar Interface dos Botões
        MousePos = pygame.mouse.get_pos()
        self.buttonButOpenBuild.update()
        self.buttonButOpenBuild.onMouseEnter(MousePos)
        self.buttonButOpenClear.update()
        self.buttonButOpenClear.onMouseEnter(MousePos)
        self.buttonButUseGrid.update()
        self.buttonButUseGrid.onMouseEnter(MousePos)

        if(ct.idFinal != None and ct.idStart != None):
            self.buttonButOpenPlay.update()
            self.buttonButOpenPlay.onMouseEnter(MousePos)

    def CalculeDistaceFromEnd(self):
        #Algoritimo para Calcular distancia ate o Objetivo.
        origemNodeList = [(ct.centerFinalPos,1)]  

        def insertNewNodeInList(pos):
            if(pos in ct.mapIdDistaceFromEnd and ct.mapIdDistaceFromEnd[pos] == 0):
                ct.mapIdDistaceFromEnd[pos] = distance
                newNodeList.append((pos,distance))


        if(ct.centerFinalPos in ct.mapIdDistaceFromEnd):
            ct.mapIdDistaceFromEnd[ct.centerFinalPos] = 0
           
            while origemNodeList:
              
                newNodeList = []
                
                for value in origemNodeList:   
                  
                    posCurrect = value[0]
                    distance = value[1] + 1
                    ct.mapIdDistaceFromEnd[posCurrect] = value[1]     
                
                    #Direita
                    insertNewNodeInList((posCurrect[0] + 1,posCurrect[1]))

                    #Esquerda      
                    insertNewNodeInList((posCurrect[0] -1,posCurrect[1]))

                    #Baixo
                    insertNewNodeInList((posCurrect[0],posCurrect[1]+1))
 
                    #Cima
                    insertNewNodeInList((posCurrect[0],posCurrect[1]-1))

                origemNodeList.clear()
                
                for ss in newNodeList:
                    origemNodeList.append(ss)
    
    def createMapId(self):
        #Configurar Colisão no Cenario
        for x in range(ct.gameWidth):
            for y in range(ct.gameHeight):
                ct.mapId[(x,y)] = 1

    def clarMap(self):
        #Restaurar Cenario
        ct.scenaryAll.clear()
        ct.scenaryRoad.clear()
        ct.StartPos = None
        ct.FinalPos = None
        ct.idStart = None
        ct.idFinal = None
        ct.mapId.clear()
        self.createMapId()

    def CancelBuild(self):
        #Cancelar Construção
        self.stateBuild = True if self.stateBuild == False else False
        self.buttonButOpenBuild.labelInput = "BUILD" if self.stateBuild == False else "CLOSE"

    def eventsButs(self):
        #Verificar Interação com os Botões
        if self.inBuild:
            return

        MousePos = pygame.mouse.get_pos()
        if self.buttonButOpenBuild.checkInput(MousePos):
            self.CancelBuild()

        if self.buttonButOpenClear.checkInput(MousePos):
            self.clarMap()          
            ct.initBoard()

        if self.buttonButUseGrid.checkInput(MousePos):
            self.useGrid = True if self.useGrid == False else False
           

        if self.buttonButOpenPlay.checkInput(MousePos):
            self.inGame = True
            ct.inGame = True
            self.useGrid = False
            self.CalculeDistaceFromEnd()
            self.NeuralNetWorking.createCars(25,True)

    def createInterfaceMenu(self):
        #Criar Interface dos Menus
        self.buttonModelImage = pygame.image.load(ct.dicImageBut2)
        self.buttonModelImage = pygame.transform.scale(self.buttonModelImage,(115,35))

        self.backgroundMenuButtons = pygame.image.load(ct.dicImageBut2)
        self.backgroundMenuButtons = pygame.transform.scale(self.backgroundMenuButtons,(268/2,337/2))
        self.backgroundMenuButtonsRenderized = self.windows.blit(self.backgroundMenuButtons,(1565,25))
        
        posButsX,posButsY = self.backgroundMenuButtonsRenderized.topright

        self.buttonButOpenBuild = bt.Button(self.buttonModelImage,posButsX - 65,posButsY + 25,"CLOSE",self.windows)
        self.buttonButOpenClear = bt.Button(self.buttonModelImage,posButsX - 65,posButsY + 65,"CLEAR",self.windows)
        self.buttonButUseGrid = bt.Button(self.buttonModelImage,posButsX - 65,posButsY + 105,"GRID",self.windows)
        self.buttonButOpenPlay = bt.Button(self.buttonModelImage,posButsX - 65,posButsY + 145,"START",self.windows)

        #Menu Build
        self.createMapMenuBuild = ctMapMenuBuild.CreateMapMenuBuild(self)
        self.createMapMenuBuild.createInterfaceMenu()

        self.createMapMenuBuildBrush =  brush.MenuBrush()

    def createMensageCancelBuild(self):
        #Definir Mensagem de Cancelar Construção
        self.backGroundMenuIfor = pygame.image.load(ct.dicBackGroundImageMenu4)
        self.backGroundMenuIfor = pygame.transform.scale(self.backGroundMenuIfor,(400,45))
        self.backGroundMenuIforRenderized = self.windows.blit(self.backGroundMenuIfor,(1320,935))
        self.labelText = ct.menuFont.render(ct.nameCancelBuild,True,"white")
        posButsX,posButsY = self.backGroundMenuIforRenderized.topleft
        self.windows.blit(self.labelText,(posButsX + 10 ,posButsY + 10))
    
    def checkBuild(self):
        #Verificar se Está Modo CONSTRUÇÃO ou Em SIMULAÇÃO
        if self.inBuild:
            self.stateBuild = False
            self.createMensageCancelBuild()

            if(self.itemBuildController.itemBuild.idType == 0):
                self.createMapMenuBuildBrush.update()

            if pygame.mouse.get_pressed()[2] or self.itemBuildController.update() == True:
                self.stateBuild = True
                self.inBuild = False
        else:
            self.backgroundMenuButtonsRenderized = self.windows.blit(self.backgroundMenuButtons,(1565,25))
            self.controllerButs()

    def update(self):
        #Atualizar o Tempo Todo
        if(self.useGrid):
            self.createInteractionGrild()

        if(self.inGame == False):
            self.checkBuild()
        else:
            self.NeuralNetWorking.update()

        if self.stateBuild == True and self.inGame == False:
            self.createMapMenuBuild.update()
 
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.eventsButs()
            if event.type == pygame.KEYDOWN:
                if(self.itemBuildController != None and self.inBuild):
                    if(self.itemBuildController.itemBuild.idType == 0):
                        if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                            ct.sizeRoad = (ct.sizeRoad[0]+5,ct.sizeRoad[1]+5)
                        elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                            ct.sizeRoad = (ct.sizeRoad[0]-5,ct.sizeRoad[1]-5)
       
        