import pygame
from Player import *
from Ghost import *
from LitleGhost import *
import flocking
class Game:
    def __init__(self):
        pygame.init()
        self.gameOver=False
        self.window=pygame.display.set_mode([1200,800])
        pygame.display.set_caption("PAKMAN LV2")
        self.clock=pygame.time.Clock()
        self.player=Player()
        self.ghost=Ghost(450,150)
        self.litleGhost=[LitleGhost(100+(i*50),500) for i in range(3)]
        self.loadImages()
        self.background = pygame.Surface(self.window.get_size())
        self.background = self.background.convert()
        self.background.fill((0,0,0))
        self.flocking=flocking.flocking([self.ghost]+self.litleGhost)
        self.timePWUP=0
        self.timeInitPWUP=100
        self.timeFinishiPWUP=150
        self.powerUp=pygame.sprite.Sprite()
        self.powerUp.image=self.powerUpImage
        self.powerUp.rect=self.powerUpImage.get_rect()
        
    def addLittleGhost(self):
        self.litleGhost.append(LitleGhost(100,500))
        self.flocking=flocking.flocking([self.ghost]+self.litleGhost)

    def removeLittleGhost(self):
        print(len(self.litleGhost))
        obj=self.litleGhost.pop()
        del(obj)
        self.flocking=flocking.flocking([self.ghost]+self.litleGhost)

    def loadImages(self):
        self.wallImage=pygame.image.load("images/wall.png")
        self.playerImage=pygame.image.load("images/snake.png")
        self.obstaculo1Image=pygame.image.load("images/obstaculo1.png")
        self.obstaculo2Image=pygame.image.load("images/obstaculo2.png")
        self.powerUpImage=pygame.image.load("images/PWUP.png")
        
    def start(self):
        while(not self.gameOver):
            a=pygame.event.get()
            for event in a:
                if (event.type == pygame.QUIT):
                    self.gameOver=True
                if(event.type==pygame.KEYDOWN):
                    if(event.key in [pygame.K_RIGHT,pygame.K_LEFT,pygame.K_DOWN,pygame.K_UP]):
                        self.player.moveKeyDown(event.key)
                if(event.type==pygame.KEYUP):
                    if(event.key in [pygame.K_RIGHT,pygame.K_LEFT,pygame.K_DOWN,pygame.K_UP]):
                        self.player.moveKeyUp(event.key)
            self.player.move()
            self.flocking.computeAlignaments() #
            self.flocking.computeCohesion() #
            self.flocking.computeSeparation() #
            self.flocking.copyComputation() #
            self.ghost.move(self.player.rect.left,self.player.rect.top)
            for i in self.litleGhost:
                i.move(self.ghost.rect.left,self.ghost.rect.top)
            self.clock.tick(25)
            if(self.timePWUP==self.timeInitPWUP):
                self.powerUp.rect.top=100;self.powerUp.rect.left=500
            if(self.timePWUP>=self.timeFinishiPWUP):
                self.timePWUP=0
            self.window.blit(self.background,(0,0))
            if(self.timePWUP>=self.timeInitPWUP):
                self.window.blit(self.powerUp.image,self.powerUp.rect)
            if(self.player.rect.colliderect(self.powerUp.rect)):
                self.timePWUP=0;self.powerUp.rect.top=-100;self.powerUp.rect.left=-100
                self.removeLittleGhost()
            elif(self.ghost.rect.colliderect(self.powerUp.rect)):
                self.timePWUP=0;self.powerUp.rect.top=-100;self.rect.left=-100
                self.addLittleGhost()
            self.window.blit(self.player.image,self.player.rect)
            self.window.blit(self.ghost.image,self.ghost.rect)
            for i in self.litleGhost:
                self.window.blit(i.image,i.rect)
            pygame.display.update()
            self.timePWUP+=1
