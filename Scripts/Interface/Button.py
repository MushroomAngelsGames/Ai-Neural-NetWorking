from . import Constants as ct
import pygame

#Criar Botões
class Button():
    def __init__(self,image,posX,posY,labelText,screen,iconBut = None, panding = 0 ) -> None:
        #Construtor
        self.screen = screen
        self.image = image
        self.posX = posX
        self.porY = posY
        self.rect = self.image.get_rect(center=(self.posX,self.porY))
        self.labelInput = labelText
        self.labelText = ct.menuFont.render(self.labelInput,True,"white")
        self.labelRect= self.labelText.get_rect(center=(self.posX,self.porY + 10 + panding))   
        self.iconBut  = None

        self.effectClick = pygame.mixer.Sound(".\Music/But.wav")

        if iconBut != None:
            self.iconBut = iconBut   
            self.rectIcon = self.iconBut.get_rect(center=(self.posX,self.porY - 10))
        pass

    def update(self):
        #Atualizar Botão na Inteface
        self.screen.blit(self.image,self.rect)
        if self.iconBut != None:
            self.screen.blit(self.iconBut,self.rectIcon)
        self.screen.blit(self.labelText,self.labelRect)

    def checkInput(self,position):
        #Verificar se o Botão foi Clicado
        if position[0] in range(self.rect.left,self.rect.right) and position[1] in range(self.rect.top,self.rect.bottom):
            self.effectClick.play()
            return True

    def onMouseEnter(self,position):
        #Animação do Mouse em Cima do Botão
        if position[0] in range(self.rect.left,self.rect.right) and position[1] in range(self.rect.top,self.rect.bottom):
            self.labelText = ct.menuFont.render(self.labelInput,True,"black")
            return True
        else :
            self.labelText = ct.menuFont.render(self.labelInput,True,"white")
            return False
      
            
