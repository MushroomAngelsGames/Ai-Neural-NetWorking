import pygame 
import Interface.Constants as ct
import Objects.Scenary as sc
from pygame.locals import *

#Controlador das Construções
class Build():
    def __init__(self,itemValue) -> None:
        #Construtor
        self.windows = pygame.display.get_surface()
        self.itemBuild = itemValue
        self.timeBuild = 0
        self.effectBuild = pygame.mixer.Sound(".\Music/build.wav")
        self.effectBuild.set_volume(1)
        pass

    def calculeCollisor(self,pos):
        #Atribuir Tipo Dos Items para Sua Respectiva Posição no Cenario

        if(self.itemBuild.idType == 0):
            for x in range(ct.sizeRoad[0]):
                for y in range(ct.sizeRoad[1]):
                    ct.mapIdDistaceFromEnd[(pos[0] + x,pos[1] + y)] = 0
                    if(ct.mapId[(pos[0] + x,pos[1] + y)] == 1):
                        ct.mapId[(pos[0] + x,pos[1] + y)] = self.itemBuild.idType
          
        else:
            for x in range(self.itemBuild.size[0]):
                for y in range(self.itemBuild.size[1]):
                    ct.mapId[(pos[0] + x,pos[1] + y)] = self.itemBuild.idType

    def resetScenary(self,pos):
        #Restaurar Map quando troca o local de Chegada
        for x in range(self.itemBuild.size[0]):
            for y in range(self.itemBuild.size[1]):             
                ct.mapId[(pos[0] + x,pos[1] + y)] = 1

    def update(self):    
        #Criar Nova Construção ao Clicar no Mouse 0
        ct.sizeRoad
        pos = pygame.mouse.get_pos()
        icone = None
        if(self.itemBuild.idType != 0):
            self.itemBuild.itemIcone = pygame.transform.scale(self.itemBuild.itemIcone, self.itemBuild.size)
            icone = self.itemBuild.itemIcone
        else:
            icone = pygame.image.load(self.itemBuild.urlImage)
            icone = pygame.transform.scale(icone, ct.sizeRoad)

        render = self.windows.blit(icone,(pos[0],pos[1]))
       
        if pygame.mouse.get_pressed()[0] and self.timeBuild > 20:     
            
            needUpdateFinal = False
            needUpdateStart = False

            if (self.itemBuild.canBuildContinues == False) :
               self.timeBuild = 0
               self.effectBuild.play()

            if (self.itemBuild.id == 2) :
                ct.StartPos = (pos[0],pos[1])
                if(ct.idStart != None):
                    self.resetScenary(ct.scenaryAll[ct.idStart].pos)
                    ct.scenaryAll[ct.idStart].pos = (pos[0],pos[1])

                    self.calculeCollisor((pos[0],pos[1]))
                    return True
                needUpdateStart  = True
            elif (self.itemBuild.id == 3) :
                ct.FinalPos = (pos[0],pos[1])
                ct.centerFinalPos = render.center
                if(ct.idFinal != None):
                    self.resetScenary(ct.scenaryAll[ct.idFinal].pos)
                    ct.scenaryAll[ct.idFinal].pos = (pos[0],pos[1])
                   
                    self.calculeCollisor((pos[0],pos[1]))
                    return True
                needUpdateFinal = True
                
            if(self.itemBuild.id != 0):
                ct.scenaryAll.append(sc.Scenary(self.itemBuild,icone,self.itemBuild.idType,(pos[0],pos[1]),self.itemBuild.size))
            else:
                ct.scenaryRoad.append(sc.Scenary(self.itemBuild,icone,self.itemBuild.idType,(pos[0],pos[1]),self.itemBuild.size))

            self.calculeCollisor((pos[0],pos[1]))

            if(needUpdateFinal):
                 ct.idFinal = len(ct.scenaryAll) - 1
                 return True
            if(needUpdateStart):
                ct.idStart = len(ct.scenaryAll) - 1
                return True
               
            return False
        else :
            self.timeBuild += 1
            return False
            
