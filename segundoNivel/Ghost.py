import pygame
import flocking
class Ghost(pygame.sprite.Sprite,flocking.agent):
    def __init__(self,x=500,y=500):
        self.image=pygame.image.load("images/monster_green.png")
        self.rect=self.image.get_rect()
        self.rect.top=x
        self.rect.left=y
        flocking.agent.__init__(self,x,y,0,0)
        self.t=0
    def move(self,playerX,playerY):
        if(self.t==0):
            self.oldPos=(self.rect.left,self.rect.top)
            dx=playerX-self.rect.left
            dy=playerY-self.rect.top
            if(dy!=0 or dx!=0):
                d=(dx/abs(float((dy**2+dx**2)**(1/2.0))),dy/abs(float((dy**2+dx**2)**(1/2.0))))
                self.velX=d[0]
                self.velY=d[1]
                self.posX=self.rect.left
                self.posY=self.rect.top
                self.rect.move_ip(d[0]*9,d[1]*9)
        else:
            self.t-=1
    def restorePosition(self):
        self.rect.left=self.oldPos[0]
        self.rect.top=self.oldPos[1]
    def pause(self):
        self.t=100