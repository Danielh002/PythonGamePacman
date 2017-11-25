import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.row=0
        self.column=0
        self.orientation="RIGHT"
        self.image=pygame.image.load("images/snake.png")
        self.rect=self.image.get_rect()
        self.rect.top=100
        self.rect.left=100
        self.rightPressed=False
        self.leftPressed=False
        self.upPressed=False
        self.downPressed=False
    def moveKeyUp(self,key):
        if(key==pygame.K_RIGHT):
            self.rightPressed=False
        if(key==pygame.K_LEFT):
            self.leftPressed=False
        if(key==pygame.K_UP):
            self.upPressed=False
        if(key==pygame.K_DOWN):
            self.downPressed=False
    def moveKeyDown(self,key):
        if(key==pygame.K_RIGHT):
            self.rightPressed=True
        if(key==pygame.K_LEFT):
            self.leftPressed=True
        if(key==pygame.K_UP):
            self.upPressed=True
        if(key==pygame.K_DOWN):
            self.downPressed=True
    def restorePosition(self):
        self.rect.left=self.oldPos[0]
        self.rect.top=self.oldPos[1]
    def moveLeft(self):
        self.column-=1
    def moveUp(self):
        self.row-=1
    def moveDown(self):
        self.row+=1
    def getPos(self):
        return (self.row,self.column)
    def move(self):
        self.oldPos=(self.rect.left,self.rect.top)
        if(self.rightPressed):
            self.rect.move_ip(10,0)
        if(self.leftPressed):
            self.rect.move_ip(-10,0)
        if(self.upPressed):
            self.rect.move_ip(0,-10)
        if(self.downPressed):
            self.rect.move_ip(0,10)