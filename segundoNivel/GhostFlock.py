import pygame
class GhostFlock (pygame.sprite.Sprite):
    def __init__(self):
        self.image=pygame.image.load("images/monster_green.png")
        self.rect=self.image.get_rect()
        self.rect.top=500
        self.rect.left=500