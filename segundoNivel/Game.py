import pygame
from Player import *
from Ghost import *
from LitleGhost import *
class Game:
    def __init__(self):
        pygame.init()
        self.gameOver=False
        self.window=pygame.display.set_mode([1200,800])
        pygame.display.set_caption("PAKMAN LV2")
        self.clock=pygame.time.Clock()
        self.player=Player()
        self.ghost=Ghost()
        self.litleGhost=[LitleGhost(100+(i*50),500) for i in range(3)]
        self.loadImages()
        self.background = pygame.Surface(self.window.get_size())
        self.background = self.background.convert()
        self.background.fill((0,0,0))
        

    def loadImages(self):
        self.wallImage=pygame.image.load("images/wall.png")
        self.playerImage=pygame.image.load("images/snake.png")
    
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
            self.ghost.move(self.player.rect.left,self.player.rect.top)
            for i in self.litleGhost:
                i.move(self.ghost.rect.left,self.ghost.rect.top)
            self.clock.tick(25)
            self.window.blit(self.background,(0,0))
            self.window.blit(self.player.image,self.player.rect)
            self.window.blit(self.ghost.image,self.ghost.rect)
            for i in self.litleGhost:
                self.window.blit(i.image,i.rect)
            pygame.display.update()
