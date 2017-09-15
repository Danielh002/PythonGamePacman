#! /usr/bin/env python

from basicMonster import *


class OrangeMonster(Monster):
   
    def __init__(self, centerPoint, image, scared_image=None):
        Monster.__init__(self,centerPoint, image, scared_image=None)

    def update(self,block_group,posObjetivoX
        , posObjetivoY, posXMonter, posYMonster, tablero):
        ##if self.scared != scared:    
        start, finish = (posXMonter,posYMonster),(posObjetivoX, posObjetivoY)
        pathfinder = AStar( tablero, start, finish, h)
        pathfinder.reverse()
        print pathfinder[0], pathfinder[1]
        direction = self.calculateDirection( pathfinder[0][0],  pathfinder[0][1], pathfinder[1][0],  pathfinder[1][1])
        xMove,yMove = 0,0 
        if self.direction==1:
            xMove = -self.dist
        elif self.direction==2:
            yMove = -self.dist
        elif self.direction==3:
            xMove = self.dist
        elif self.direction==4:
            yMove = self.dist
        self.rect.move_ip(xMove,yMove) #Move the Rect

    def calculateDirection(self, filaInical, columnaInicial, fila , col  ):
        return Monster.calculateDirection(self, filaInical, columnaInicial, fila , col)

    def SetScared(self, scared):
        Monster.SetScared(self, scared)

    def Eaten(self):
        Monster.Eaten(self)