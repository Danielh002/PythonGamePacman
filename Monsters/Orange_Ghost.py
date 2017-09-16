#! /usr/bin/env python

from basicMonster import *


class OrangeMonster(Monster): 
   
    def __init__(self, centerPoint, image, scared_image=None):
        Monster.__init__(self,centerPoint, image, scared_image=None)

    def update(self, block_group, posObjetivoX
        , posObjetivoY, posXMonster, posYMonster, tablero):
        start = (posXMonster, posYMonster)
        finish = (posObjetivoX, posObjetivoY)
        xMove,yMove = 0,0
        if self.scared != True :    
            pathfinder = checkVF( tablero, start, finish)
            if ( pathfinder!= False):
                if ( len(pathfinder)>1 ):
                    self.direction = self.calculateDirection( pathfinder[-1][0],  pathfinder[-1][1], pathfinder[-2][0],  pathfinder[-2][1])
                    #Izquierda direction = 1
                    if self.direction==1:
                        xMove = -self.dist
                    #Abajo direction = 2
                    elif self.direction==2:
                        yMove = -self.dist
                    #Derecha direction = 3
                    elif self.direction==3:
                        xMove = self.dist
                    #Arriba direction = 4
                    elif self.direction==4:
                        yMove = self.dist
                    self.rect.move_ip(xMove,yMove) #Move the Rect
            else:
                #Izquierda direction = 1
                if self.direction==1:
                    xMove = -self.dist
                #Abajo direction = 2
                elif self.direction==2:
                    yMove = -self.dist
                #Derecha direction = 3
                elif self.direction==3:
                    xMove = self.dist
                #Arriba direction = 4
                elif self.direction==4:
                    yMove = self.dist      
                self.rect.move_ip(xMove,yMove) #Move the Rect
                self.moveCount += 1 #Update the Move count
                if pygame.sprite.spritecollideany(self, block_group):
                    """IF we hit a block, don't move - reverse the movement"""
                    self.rect.move_ip(-xMove,-yMove)
                    self.direction = random.randint(1,4)
                elif self.moves == self.moveCount:
                    """If we have moved enough, choose a new direction"""
                    self.direction = random.randint(1,4)
                    self.moves = random.randint(100,200)
                    self.moveCount = 0; 

    def calculateDirection(self, filaInical, columnaInicial, fila , col ):
        return Monster.calculateDirection(self, filaInical, columnaInicial, fila , col)

    def SetScared(self, scared):
        Monster.SetScared(self, scared)

    def Eaten(self):
        Monster.Eaten(self)

    def Move(self, direction):
        Monster.Move(self, direction)

    def PosicionInversa(self, posX , posY):
        return Monster.PosicionInversa(self, posX, posY)