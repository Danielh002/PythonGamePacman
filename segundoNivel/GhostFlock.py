import pygame
import flocking
class GhostFlock (pygame.sprite.Sprite,flocking.agent):
    def __init__(self,posX,posY,velX,velY):
        self.image=pygame.image.load("images/monster_green.png")
        self.rect=self.image.get_rect()
        self.rect.top=500
        self.rect.left=500
        super(flocking.agent,self).__init__(posX,posY,velX,velY)