#! /usr/bin/env python

from basicMonster import *


class PinkMonster(Monster): 
   
    def __init__(self, centerPoint, image, scared_image=None):
        Monster.__init__(self,centerPoint, image, scared_image)

    def update(self, block_group, posObjetivoX
        , posObjetivoY, posXMonter, posYMonster, tablero):
        if self.scared != True:    
            start, finish = (posXMonter,posYMonster),(posObjetivoX, posObjetivoY)
        else:
            start = (posXMonter,posYMonster)
            finish = self.PosicionInversa(posXMonter, posYMonster)

        pathfinder = AStar( tablero, start, finish, h)
        if ( pathfinder != False ):
            if ( len(pathfinder) > 1): 
                self.direction = self.calculateDirection( pathfinder[-1][0],  pathfinder[-1][1], pathfinder[-2][0],  pathfinder[-2][1])
                xMove,yMove = 0,0
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

    #def Adelantar(self, filaInical, columnaInicial, filaFinal , colFinal)
