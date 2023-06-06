import pygame

#Class Responsavel por Inicializar os dados dos Items no Jogo
class ItemBuildClass():
    def __init__(self,id,dicIcone,name,descriptionItem,size,idType,canBuildContinues) -> None:
        self.id = id
        self.itemIcone = pygame.image.load(dicIcone)
        self.name = name
        self.But = None
        self.descriptionItem = descriptionItem
        self.size =size
        self.idType = idType
        self.urlImage = dicIcone
        self.canBuildContinues = canBuildContinues
        pass