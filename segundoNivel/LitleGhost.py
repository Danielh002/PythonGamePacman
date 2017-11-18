import pygame
import flocking
class LitleGhost(pygame.sprite.Sprite,flocking.agent):
    def __init__(self,x=500,y=500):
        self.image=pygame.image.load("images/monster_green.png")
        self.rect=self.image.get_rect()
        self.rect.top=y
        self.rect.left=x
        flocking.agent.__init__(self,x,y,0,0)
    def move(self,playerX,playerY):
        self.rect.move_ip(self.velX*9,self.velY*9)
        self.posX,self.posY=self.rect.left,self.rect.top
        # dx=playerX-self.rect.left
        # dy=playerY-self.rect.top
        # if(dy!=0 or dx!=0):
        #     d=(dx/abs(float((dy**2+dx**2)**(1/2.0))),dy/abs(float((dy**2+dx**2)**(1/2.0))))
        #     self.rect.move_ip(d[0]*8.5,d[1]*8.5)